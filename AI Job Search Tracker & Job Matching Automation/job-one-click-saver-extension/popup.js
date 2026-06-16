// const webhookUrl =
//   "https://n8n-miglearn.onrender.com/webhook-test/job-one-click-saver";

// Later, when your n8n workflow is active, change it to:
const webhookUrl =
  "https://n8n-miglearn.onrender.com/webhook/job-one-click-saver";

const saveBtn = document.getElementById("saveBtn");
const statusBox = document.getElementById("status");

function setStatus(message, type = "") {
  statusBox.textContent = message;
  statusBox.className = type;
}

saveBtn.addEventListener("click", async () => {
  setStatus("Capturing page...", "loading");
  saveBtn.disabled = true;

  try {
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true,
    });

    const results = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => {
        function cleanText(text) {
          return (text || "")
            .replace(/\r/g, "\n")
            .replace(/\n{3,}/g, "\n\n")
            .replace(/[ \t]{2,}/g, " ")
            .trim();
        }

        function getDomain() {
          return window.location.hostname.replace(/^www\./, "");
        }

        function getPlatform(domain) {
          if (domain.includes("jobstreet")) return "JobStreet";
          if (domain.includes("indeed")) return "Indeed";
          if (domain.includes("linkedin")) return "LinkedIn";
          if (domain.includes("onlinejobs")) return "OnlineJobs.ph";
          return "Other";
        }

        function getTextFromSelectors(selectors) {
          for (const selector of selectors) {
            const el = document.querySelector(selector);
            const text = cleanText(el?.innerText || el?.textContent || "");

            if (text) {
              return text;
            }
          }

          return "";
        }

        const domain = getDomain();
        const platform = getPlatform(domain);

        const url = window.location.href;
        const title = document.title;
        const savedAt = new Date().toISOString();

        const detectedJobTitle = getTextFromSelectors([
          '[data-automation="job-detail-title"]',
          '[data-automation="jobDetailsHeader"] h1',
          '[data-testid="jobsearch-JobInfoHeader-title"]',
          ".jobsearch-JobInfoHeader-title",
          ".top-card-layout__title",
          ".jobs-unified-top-card__job-title",
          ".jobs-details__main-content h1",
          "h1",
        ]);

        const detectedCompany = getTextFromSelectors([
          '[data-automation="advertiser-name"]',
          '[data-automation="jobCompany"]',
          '[data-automation="company-name"]',
          '[data-testid="inlineHeader-companyName"]',
          ".jobsearch-InlineCompanyRating a",
          ".jobsearch-CompanyInfoWithoutHeaderImage",
          ".topcard__org-name-link",
          ".jobs-unified-top-card__company-name",
        ]);

        // 1. Best option: highlighted text
        const selectedText = cleanText(window.getSelection().toString());

        if (selectedText && selectedText.length > 200) {
          const combinedSelectedText = cleanText(`
${detectedJobTitle}
${detectedCompany}

${selectedText}
`);

          return {
            url,
            title,
            domain,
            platform,
            jobTitleHint: detectedJobTitle,
            companyHint: detectedCompany,
            text: combinedSelectedText.slice(0, 50000),
            captureMethod: "selected_text",
            detectedSelector: "window.getSelection()",
            textLength: combinedSelectedText.length,
            savedAt,
          };
        }

        // 2. Detect actual job detail panel
        const selectors = [
          // JobStreet / SEEK
          '[data-automation="jobAdDetails"]',
          '[data-automation="jobDetailsPage"]',
          '[data-automation="job-detail"]',
          '[data-testid="job-detail"]',
          '[data-testid="job-details"]',

          // Indeed
          "#jobDescriptionText",
          '[data-testid="jobsearch-JobComponent"]',
          ".jobsearch-JobComponent",

          // LinkedIn
          ".jobs-search__job-details",
          ".jobs-details",
          ".jobs-description",
          ".jobs-box__html-content",
          ".jobs-description-content__text",

          // OnlineJobs.ph / generic
          ".job-description",
          ".job-details",
          ".job-detail",
          ".description",
          "article",
          "main",
        ];

        let bestText = "";
        let bestSelector = "";

        for (const selector of selectors) {
          const elements = Array.from(document.querySelectorAll(selector));

          for (const el of elements) {
            const text = cleanText(el.innerText);

            if (text.length > bestText.length) {
              bestText = text;
              bestSelector = selector;
            }
          }
        }

        // 3. No full-page fallback
        if (!bestText || bestText.length < 500) {
          return {
            url,
            title,
            domain,
            platform,
            jobTitleHint: detectedJobTitle,
            companyHint: detectedCompany,
            text: "",
            captureMethod: "failed_no_job_panel",
            detectedSelector: "",
            textLength: 0,
            savedAt,
            error:
              "Could not detect a single job post. Highlight the job description text, then click Save again.",
          };
        }

        const combinedText = cleanText(`
${detectedJobTitle}
${detectedCompany}

${bestText}
`);

        return {
          url,
          title,
          domain,
          platform,
          jobTitleHint: detectedJobTitle,
          companyHint: detectedCompany,
          text: combinedText.slice(0, 50000),
          captureMethod: "detected_job_panel",
          detectedSelector: bestSelector,
          textLength: combinedText.length,
          savedAt,
        };
      },
    });

    const payload = results[0]?.result;

    if (!payload) {
      throw new Error("No page data captured.");
    }

    if (payload.error || !payload.text) {
      throw new Error(payload.error || "No job text captured.");
    }

    setStatus("Sending to n8n...", "loading");

    const response = await fetch(webhookUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const responseText = await response.text();

    if (!response.ok) {
      throw new Error("n8n returned " + response.status + ": " + responseText);
    }

    let result = {};

    try {
      result = JSON.parse(responseText);
    } catch (error) {
      result = {};
    }

    const message =
      result.message ||
      (result.action === "created"
        ? "New job saved to Airtable."
        : result.action === "updated"
          ? "Existing job updated in Airtable."
          : "Job saved successfully.");

    setStatus(message, "success");
  } catch (error) {
    setStatus("Error: " + error.message, "error");
  } finally {
    saveBtn.disabled = false;
  }
});

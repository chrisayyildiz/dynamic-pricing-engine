(function () {
  // Generate an anonymised session ID (do NOT link to login/user ID)
  const sessionId = crypto.randomUUID();
  
  // Capture entry timestamp
  const timeStart = Date.now();

  // Detect device type
  const deviceType = /Mobile|Android|iPhone/.test(navigator.userAgent) ? "mobile" : "desktop";

  // Local time in hours
  const localTime = new Date().getHours();

  // Language preference
  const language = navigator.language || "unknown";

  // Currency (example: assumes you have a #currency-selector element)
  const getCurrency = () => {
    const el = document.querySelector('#currency-selector');
    return el ? el.value : "unknown";
  };

  // Track click events for urgency estimation
  const clickEvents = [];
  document.addEventListener("click", (e) => {
    clickEvents.push({
      time: Date.now(),
      tag: e.target.tagName,
      id: e.target.id || null,
      class: e.target.className || null
    });
  });

  // On page unload, send all data to backend
  window.addEventListener("beforeunload", () => {
    const payload = {
      sessionId: sessionId,
      timeSpent: (Date.now() - timeStart) / 1000, // in seconds
      deviceType: deviceType,
      localTime: localTime,
      language: language,
      currency: getCurrency(),
      clickEvents: clickEvents,
    };

    // Send data to backend (asynchronously, non-blocking)
    navigator.sendBeacon("/api/track", JSON.stringify(payload));
  });
})();

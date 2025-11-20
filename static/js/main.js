// Wait until DOM is ready
document.addEventListener("DOMContentLoaded", function () {
  console.log('JavaScript file loaded successfully!');

  /* Mobile Menu Toggle */
  const menuToggle = document.getElementById("menu-toggle");
  const navLinks = document.getElementById("nav-links");
  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");
    });
  }

  /* Tabs in Help Section */
  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');
  
  tabButtons.forEach(button => {
    button.addEventListener('click', function() {
      const targetId = this.getAttribute('data-target');
      
      console.log('Tab clicked:', targetId); // Debug log
      
      // Remove active class from all buttons and contents
      tabButtons.forEach(btn => {
        btn.classList.remove('active', 'bg-pink-100');
      });
      tabContents.forEach(content => {
        content.classList.remove('active');
      });
      
      // Add active class to clicked button and corresponding content
      this.classList.add('active', 'bg-pink-100');
      const targetContent = document.getElementById(targetId);
      if (targetContent) {
        targetContent.classList.add('active');
        console.log('Activated tab:', targetId); // Debug log
      } else {
        console.error('Tab content not found:', targetId); // Debug log
      }
    });
  });

  /* Report Form Handling */
  const reportForm = document.getElementById("reportForm");
  const reportMessage = document.getElementById("reportMessage");

  if (reportForm) {
    console.log("Report form found!"); // Debug
    reportForm.addEventListener("submit", async (e) => {
      e.preventDefault(); // Prevent default form submission
      console.log("Form submitted!"); // Debug

      const reportData = {
        name: document.getElementById("name").value,
        contact: document.getElementById("contact").value,
        email: document.getElementById("email").value || "Not provided",
        incident: document.getElementById("incident-type").value,
        location: document.getElementById("location").value,
        urgency_level: document.getElementById("urgency-level").value,
        description: document.getElementById("description").value,
        support_needed: Array.from(document.querySelectorAll('input[type="checkbox"]:checked')).map(cb => cb.value),
        anonymous: document.getElementById("anonymous").checked || false
      };


      // basic validation
      if (!reportData.name || !reportData.phone || !reportData.location || !reportData.description) {
        reportMessage.textContent = "Please fill in all required fields.";
        reportMessage.style.color = "red";
        return;
      }

      try {
        const res = await fetch("/api/report", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(reportData),
        });

        if (res.ok) {
          reportMessage.textContent = "Your report has been submitted successfully.";
          reportMessage.style.color = "green";
          reportForm.reset();
        } else {
          const err = await res.json().catch(()=>({}));
          reportMessage.textContent = err.error || "Something went wrong. Please try again.";
          reportMessage.style.color = "red";
        }
      } catch (err) {
        console.error(err);
        reportMessage.textContent = "Network or server error. Please try again later.";
        reportMessage.style.color = "red";
      }
    });
  }
});
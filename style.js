/* =========================
   Portfolio JavaScript
========================= */

// Check JS connection
console.log("JavaScript connected successfully");

// Fade-in animation on page load
window.addEventListener("load", () => {
    document.body.style.opacity = "1";
});

// Smooth scroll for future anchor links
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener("click", e => {
        e.preventDefault();
        const target = document.querySelector(link.getAttribute("href"));
        if (target) {
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
});

// Simple interaction log for skills
document.querySelectorAll(".skills span").forEach(skill => {
    skill.addEventListener("mouseenter", () => {
        console.log("Skill hovered:", skill.textContent);
    });
});

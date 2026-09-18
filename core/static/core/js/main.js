// Hero terminal typewriter loop
document.addEventListener('DOMContentLoaded', () => {
    const typedEl = document.getElementById('hero-typed');
    if (!typedEl) return;

    const lines = [
        "Python • Django • DRF • PostgreSQL • Docker • AWS",
        "building scalable REST APIs...",
"Status:Open for Internship & Freelance Projects",
    ];

    let lineIdx = 0;
    let charIdx = 0;
    let deleting = false;

    function tick() {
        const current = lines[lineIdx];

        if (!deleting) {
            charIdx++;
            typedEl.textContent = current.slice(0, charIdx);
            if (charIdx === current.length) {
                deleting = true;
                setTimeout(tick, 1600);
                return;
            }
        } else {
            charIdx--;
            typedEl.textContent = current.slice(0, charIdx);
            if (charIdx === 0) {
                deleting = false;
                lineIdx = (lineIdx + 1) % lines.length;
            }
        }
        setTimeout(tick, deleting ? 30 : 55);
    }

    setTimeout(tick, 600);
});

// Scroll-triggered fade-in for sections
document.addEventListener('DOMContentLoaded', () => {
    const revealEls = document.querySelectorAll('.reveal');
    if (!revealEls.length) return;

    if (!('IntersectionObserver' in window)) {
        revealEls.forEach(el => el.classList.add('is-visible'));
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });

    revealEls.forEach(el => observer.observe(el));

    // Safety fallback: if anything is still hidden after load
    // (e.g. stale cached script, slow observer), force-reveal it.
    window.addEventListener('load', () => {
        setTimeout(() => {
            document.querySelectorAll('.reveal:not(.is-visible)').forEach(el => {
                el.classList.add('is-visible');
            });
        }, 1200);
    });
});
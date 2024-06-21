document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll('.section');

    sections.forEach(section => {
        section.classList.add('active');
    });

    document.addEventListener('scroll', function() {
        sections.forEach(section => {
            if (isInViewport(section)) {
                section.classList.add('active');
            }
        });
    });

    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)
        );
    }
});

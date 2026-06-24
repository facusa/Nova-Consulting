document.addEventListener('DOMContentLoaded', () => {
    // 1. Sticky Navbar Effect
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 2. Active Link Highlighting on Scroll
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-links a');

    window.addEventListener('scroll', () => {
        let current = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;

            if (window.scrollY >= (sectionTop - sectionHeight / 3)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // 4. Smooth Scrolling for Anchor Links (including Back to Top)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                const navHeight = navbar.offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - navHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }

            // Cerrar el menú en móviles al hacer clic en un enlace
            const navLinksContainer = document.querySelector('.nav-links');
            if (window.innerWidth <= 768) {
                navLinksContainer.style.display = 'none';
            }
        });
    });

    // 5. Mobile Menu Toggle (Basic implementation)
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navLinksContainer = document.querySelector('.nav-links');

    mobileMenuBtn.addEventListener('click', () => {
        // Simple toggle inline style for demo purposes
        if (navLinksContainer.style.display === 'flex') {
            navLinksContainer.style.display = 'none';
        } else {
            navLinksContainer.style.display = 'flex';
            navLinksContainer.style.flexDirection = 'column';
            navLinksContainer.style.position = 'absolute';
            navLinksContainer.style.top = '100%';
            navLinksContainer.style.left = '0';
            navLinksContainer.style.width = '100%';
            navLinksContainer.style.background = 'rgba(255, 255, 255, 0.95)';
            navLinksContainer.style.backdropFilter = 'blur(16px)';
            navLinksContainer.style.padding = '24px';
            navLinksContainer.style.borderBottom = '1px solid rgba(0, 0, 0, 0.08)';
        }
    });

    // Ensure desktop menu reappears if window is resized
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            navLinksContainer.style.display = '';
            navLinksContainer.style.flexDirection = '';
            navLinksContainer.style.position = '';
            navLinksContainer.style.top = '';
            navLinksContainer.style.left = '';
            navLinksContainer.style.width = '';
            navLinksContainer.style.background = '';
            navLinksContainer.style.backdropFilter = '';
            navLinksContainer.style.padding = '';
            navLinksContainer.style.borderBottom = '';
        } else if (navLinksContainer.style.display !== 'flex') {
            navLinksContainer.style.display = 'none';
        }
    });
    
    // 6. Number Counter Animation for Impact Section
    const statsSection = document.getElementById('estadisticas');
    if (statsSection) {
        const counters = statsSection.querySelectorAll('.mv-card h2');
        
        const counterData = [];
        counters.forEach(counter => {
            const originalText = counter.innerText;
            const targetValue = parseInt(originalText.replace(/[^0-9]/g, ''));
            const prefix = originalText.replace(/[0-9].*/, '');
            const suffix = originalText.replace(/.*[0-9]/, '');
            
            counterData.push({ element: counter, target: targetValue, prefix, suffix });
            counter.innerText = `${prefix}0${suffix}`;
        });

        const animateCounters = () => {
            counterData.forEach(data => {
                const updateCount = () => {
                    const currentStr = data.element.innerText.replace(/[^0-9]/g, '');
                    const current = currentStr === '' ? 0 : parseInt(currentStr);
                    const increment = data.target / 30; // 30 steps
                    
                    if (current < data.target) {
                        data.element.innerText = `${data.prefix}${Math.ceil(current + increment)}${data.suffix}`;
                        setTimeout(updateCount, 40);
                    } else {
                        data.element.innerText = `${data.prefix}${data.target}${data.suffix}`;
                    }
                };
                updateCount();
            });
        };

        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounters();
                observer.disconnect();
            }
        }, { threshold: 0.5 });

        observer.observe(statsSection);
    }
});

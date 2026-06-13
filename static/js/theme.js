/**
 * AURORA INTERACTIVE THEME & EVENT HANDLER
 * Provides light/dark switching, dynamic ambient particle generation,
 * and responsive navigation controls.
 */

document.addEventListener("DOMContentLoaded", function () {
    const themeButton = document.getElementById("theme-toggle");
    const hamburgerMenu = document.getElementById("hamburgerMenu");
    const navMenu = document.getElementById("navMenu");

    // 1. MOBILE MENU DRAWER TOGGLE
    if (hamburgerMenu && navMenu) {
        hamburgerMenu.addEventListener("click", function () {
            navMenu.classList.toggle("active");
            
            // Toggle icons between hamburger (bars) and close (xmark)
            const icon = hamburgerMenu.querySelector("i");
            if (icon) {
                if (navMenu.classList.contains("active")) {
                    icon.classList.remove("fa-bars");
                    icon.classList.add("fa-xmark");
                } else {
                    icon.classList.remove("fa-xmark");
                    icon.classList.add("fa-bars");
                }
            }
        });
    }

    // Close mobile menu on clicking any link
    const navLinks = document.querySelectorAll(".nav-link");
    navLinks.forEach(link => {
        link.addEventListener("click", function() {
            if (navMenu && navMenu.classList.contains("active")) {
                navMenu.classList.remove("active");
                const icon = hamburgerMenu ? hamburgerMenu.querySelector("i") : null;
                if (icon) {
                    icon.classList.remove("fa-xmark");
                    icon.classList.add("fa-bars");
                }
            }
        });
    });

    // 2. THEME SWITCHER LOGIC
    if (themeButton) {
        // Load saved theme configuration from localStorage
        const savedTheme = localStorage.getItem("theme");
        if (savedTheme === "light") {
            document.body.classList.add("light");
            themeButton.innerHTML = "🌙";
        } else {
            document.body.classList.remove("light");
            themeButton.innerHTML = "☼";
        }

        themeButton.addEventListener("click", function () {
            document.body.classList.toggle("light");

            if (document.body.classList.contains("light")) {
                localStorage.setItem("theme", "light");
                themeButton.innerHTML = "🌙";
            } else {
                localStorage.setItem("theme", "dark");
                themeButton.innerHTML = "☼";
            }
        });
    }

    // 3. AMBIENT GLOW PARTICLE GENERATOR (For Rich Galactic Aesthetics)
    initAmbientParticles();
});

/**
 * Creates floating ambient glow particles inside dark mode.
 * Automatically handles sizing, random color nodes, and smooth infinite floating keyframes.
 */
function initAmbientParticles() {
    // Prevent duplicates
    const existing = document.querySelector(".dynamic-particles-wrapper");
    if (existing) existing.remove();

    const particlesContainer = document.createElement("div");
    particlesContainer.className = "dynamic-particles-wrapper";
    particlesContainer.style.position = "fixed";
    particlesContainer.style.inset = "0";
    particlesContainer.style.pointerEvents = "none";
    particlesContainer.style.zIndex = "-1";
    particlesContainer.style.overflow = "hidden";
    
    document.body.appendChild(particlesContainer);

    const particleCount = 20;
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement("div");
        const size = Math.random() * 4 + 2; // Particle sizes 2px to 6px
        
        particle.style.position = "absolute";
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.borderRadius = "50%";
        
        // Random theme palette colors (Electric Cyan, Emerald Green, Soft Violet)
        const palette = [
            "rgba(56, 189, 248, 0.25)", // Cyan
            "rgba(16, 185, 129, 0.18)", // Emerald
            "rgba(139, 92, 246, 0.15)"  // Violet
        ];
        
        const randomColor = palette[Math.floor(Math.random() * palette.length)];
        particle.style.background = randomColor;
        particle.style.boxShadow = `0 0 12px ${randomColor}`;
        
        // Randomized positions
        particle.style.top = `${Math.random() * 100}vh`;
        particle.style.left = `${Math.random() * 100}vw`;
        
        // Custom durations for parallax movement
        const duration = Math.random() * 25 + 15; // 15s to 40s
        const delay = Math.random() * -20;
        
        particle.style.animation = `floatParticleEffect ${duration}s linear infinite`;
        particle.style.animationDelay = `${delay}s`;
        
        particlesContainer.appendChild(particle);
    }

    // Append Float Animation CSS Keyframes
    const style = document.createElement("style");
    style.innerHTML = `
        @keyframes floatParticleEffect {
            0% {
                transform: translateY(0) translateX(0) scale(1);
                opacity: 0;
            }
            10% {
                opacity: 0.8;
            }
            90% {
                opacity: 0.8;
            }
            100% {
                transform: translateY(-120px) translateX(60px) scale(0.8);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
}

// ==============================
// STAR REVIEW SYSTEM
// ==============================


const stars = document.querySelectorAll(
    ".star-picker i"
);


const ratingInput = document.getElementById(
    "id_rating"
);




if(stars.length > 0 && ratingInput){


    stars.forEach(

        star => {


            star.addEventListener(

                "click",

                function(){


                    let rating = this.getAttribute(
                        "data-value"
                    );



                    ratingInput.value = rating;



                    stars.forEach(

                        s => {


                            if(

                                s.getAttribute("data-value")
                                <=
                                rating

                            ){


                                s.classList.add(
                                    "active"
                                );


                            }


                            else{


                                s.classList.remove(
                                    "active"
                                );


                            }


                        }


                    );


                }


            );


        }


    );


}
// Dark Mode Toggle Functionality

(function() {
    'use strict';

    // Get theme from localStorage or default to 'light'
    const getTheme = () => {
        return localStorage.getItem('theme') || 'light';
    };

    // Set theme
    const setTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        updateToggleIcon(theme);
    };

    // Update toggle button icon
    const updateToggleIcon = (theme) => {
        const icon = document.querySelector('.theme-toggle i');
        if (icon) {
            if (theme === 'dark') {
                icon.className = 'fa fa-sun-o';
            } else {
                icon.className = 'fa fa-moon-o';
            }
        }
    };

    // Toggle theme
    const toggleTheme = () => {
        const currentTheme = getTheme();
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        setTheme(newTheme);
    };

    // Initialize theme on page load
    const initTheme = () => {
        const theme = getTheme();
        setTheme(theme);

        // Add toggle button if it doesn't exist
        if (!document.querySelector('.theme-toggle')) {
            const toggleButton = document.createElement('button');
            toggleButton.className = 'theme-toggle';
            toggleButton.setAttribute('aria-label', 'Toggle dark mode');
            toggleButton.innerHTML = '<i class="fa fa-moon-o"></i>';
            toggleButton.addEventListener('click', toggleTheme);
            document.body.appendChild(toggleButton);
        } else {
            // If button exists, attach event listener
            document.querySelector('.theme-toggle').addEventListener('click', toggleTheme);
        }
    };

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
    } else {
        initTheme();
    }
})();

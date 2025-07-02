// backToTop.js

// Back to Top and Go to Bottom Button functionality
const backToTopBtn = document.querySelector('.back-to-top');
const goToBottomBtn = document.querySelector('.go-to-bottom');

// Show buttons when the user scrolls down
window.onscroll = function() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        backToTopBtn.style.display = 'block';  // Show back to top button
        goToBottomBtn.style.display = 'block';  // Show go to bottom button
    } else {
        backToTopBtn.style.display = 'none';  // Hide back to top button
        goToBottomBtn.style.display = 'none';  // Hide go to bottom button
    }
};

// Back to top button click event (instant jump)
backToTopBtn.addEventListener('click', function(e) {
    e.preventDefault();
    window.scrollTo(0, 0);  // Direct jump to the top
});

// Go to bottom button click event (instant jump)
goToBottomBtn.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector('#bottom').scrollIntoView(false);  // Direct jump to the bottom
});

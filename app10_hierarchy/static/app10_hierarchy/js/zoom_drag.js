
const img = document.getElementById('hierarchy-image');
const zoomContainer = document.getElementById('zoom-container');
let scale = 1;
let isDragging = false;
let startX = 0;
let startY = 0;
let translateX = 0;
let translateY = 0;
let isFullscreen = false;

// Zoom with mouse wheel
zoomContainer.addEventListener('wheel', function(e) {
    e.preventDefault();
    const delta = e.deltaY > 0 ? -0.1 : 0.1;
    const prevScale = scale;
    scale = Math.min(Math.max(1, scale + delta), 5);

    const rect = img.getBoundingClientRect();
    const offsetX = e.clientX - rect.left;
    const offsetY = e.clientY - rect.top;
    translateX = translateX - (offsetX * (scale - prevScale)) / prevScale;
    translateY = translateY - (offsetY * (scale - prevScale)) / prevScale;

    updateTransform();
});

// Dragging functionality
zoomContainer.addEventListener('mousedown', startDragging);
zoomContainer.addEventListener('mousemove', drag);
zoomContainer.addEventListener('mouseup', stopDragging);
zoomContainer.addEventListener('mouseleave', stopDragging);

// Touch support
zoomContainer.addEventListener('touchstart', handleTouchStart);
zoomContainer.addEventListener('touchmove', handleTouchMove);
zoomContainer.addEventListener('touchend', stopDragging);

function startDragging(e) {
    e.preventDefault();
    isDragging = true;
    zoomContainer.style.cursor = 'grabbing';
    startX = e.clientX - translateX;
    startY = e.clientY - translateY;
}

function drag(e) {
    if (isDragging) {
        translateX = e.clientX - startX;
        translateY = e.clientY - startY;
        updateTransform();
    }
}

function stopDragging() {
    isDragging = false;
    zoomContainer.style.cursor = 'grab';
}

function handleTouchStart(e) {
    e.preventDefault();
    if (e.touches.length === 1) {
        isDragging = true;
        zoomContainer.style.cursor = 'grabbing';
        startX = e.touches[0].clientX - translateX;
        startY = e.touches[0].clientY - translateY;
    }
}

function handleTouchMove(e) {
    if (isDragging && e.touches.length === 1) {
        translateX = e.touches[0].clientX - startX;
        translateY = e.touches[0].clientY - startY;
        updateTransform();
    }
}

function updateTransform() {
    const rect = img.getBoundingClientRect();
    const containerRect = zoomContainer.getBoundingClientRect();
    const maxTranslateX = (rect.width * scale - containerRect.width) / 2;
    const maxTranslateY = (rect.height * scale - containerRect.height) / 2;

    translateX = Math.min(Math.max(translateX, -maxTranslateX), maxTranslateX);
    translateY = Math.min(Math.max(translateY, -maxTranslateY), maxTranslateY);

    img.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
}

function toggleFullscreen() {
    const elem = document.querySelector('.image-box');
    if (!isFullscreen) {
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        } else if (elem.webkitRequestFullscreen) {
            elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) {
            elem.msRequestFullscreen();
        }
        isFullscreen = true;
        elem.querySelector('.fullscreen-icon').style.background = 'linear-gradient(135deg, #ff6b6b, #e53e3e)'; // Red gradient for exit
        elem.querySelector('.fullscreen-icon').style.transform = 'scale(1)';
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
        }
        isFullscreen = false;
        elem.querySelector('.fullscreen-icon').style.background = 'linear-gradient(135deg, #4a90e2, #357abd)'; // Back to blue gradient
    }
}

// Handle fullscreen change events
document.addEventListener('fullscreenchange', function() {
    const elem = document.querySelector('.image-box');
    if (!document.fullscreenElement) {
        isFullscreen = false;
        elem.querySelector('.fullscreen-icon').style.background = 'linear-gradient(135deg, #4a90e2, #357abd)';
        updateTransform();
    }
});

// Adjust transform on window resize
window.addEventListener('resize', updateTransform);
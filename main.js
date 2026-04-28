document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const btn = document.getElementById('mobile-menu-button');
    const menu = document.getElementById('mobile-menu');

    if (btn && menu) {
        btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
        });
    }

    // Audio Player functionality
    const audioPlayer = document.getElementById('audio-player');
    const playBtn = document.getElementById('play-btn');
    const playIcon = document.getElementById('play-icon');
    const pauseIcon = document.getElementById('pause-icon');
    const progressBar = document.getElementById('progress-bar');
    const progressContainer = document.getElementById('progress-container');
    const timeDisplay = document.getElementById('time-display');
    const visualizer = document.getElementById('audio-visualizer-container');

    if (audioPlayer && playBtn) {
        // Set volume to 50%
        audioPlayer.volume = 0.5;

        playBtn.addEventListener('click', () => {
            if (audioPlayer.paused) {
                audioPlayer.play();
                playIcon.classList.add('hidden');
                pauseIcon.classList.remove('hidden');
                if (visualizer) visualizer.classList.add('playing');
            } else {
                audioPlayer.pause();
                playIcon.classList.remove('hidden');
                pauseIcon.classList.add('hidden');
                if (visualizer) visualizer.classList.remove('playing');
            }
        });

        audioPlayer.addEventListener('timeupdate', () => {
            const percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
            if (progressBar) progressBar.style.width = `${percent}%`;
            
            // Format time
            const currentMins = Math.floor(audioPlayer.currentTime / 60);
            const currentSecs = Math.floor(audioPlayer.currentTime % 60);
            const durationMins = Math.floor(audioPlayer.duration / 60) || 1;
            const durationSecs = Math.floor(audioPlayer.duration % 60) || 0;
            
            if (timeDisplay && !isNaN(audioPlayer.duration)) {
                timeDisplay.textContent = `${currentMins}:${currentSecs.toString().padStart(2, '0')} / ${durationMins}:${durationSecs.toString().padStart(2, '0')}`;
            }
        });

        if (progressContainer) {
            progressContainer.addEventListener('click', (e) => {
                const width = progressContainer.clientWidth;
                const clickX = e.offsetX;
                const duration = audioPlayer.duration;
                audioPlayer.currentTime = (clickX / width) * duration;
            });
        }
    }
});

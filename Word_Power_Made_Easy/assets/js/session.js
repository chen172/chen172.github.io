    const tableBody = document.getElementById('tableBody');
    const cardView = document.getElementById('cardView');
    const tableView = document.getElementById('tableView');
    const toggleBtn = document.getElementById('toggleViewBtn');
    const playPauseBtn = document.getElementById('playPauseBtn');

    // Populate Table View
    entries.forEach(({ word, phonetic, audio }) => {
      const tr = document.createElement('tr');

      const tdWord = document.createElement('td');
      tdWord.classList.add('word');
      tdWord.textContent = word;

      const tdPhonetic = document.createElement('td');
      tdPhonetic.classList.add('phonetic');
      tdPhonetic.textContent = phonetic;

      const tdAudio = document.createElement('td');
      const audioEl = document.createElement('audio');
      audioEl.src = audio;
      audioEl.classList.add('audio-player');
      audioEl.preload = 'none';
      audioEl.controls = true;
      audioEl.setAttribute('aria-label', `Play audio for word ${word}`);
      tdAudio.appendChild(audioEl);

      tr.appendChild(tdWord);
      tr.appendChild(tdPhonetic);
      tr.appendChild(tdAudio);
      tableBody.appendChild(tr);
    });

    // Populate Card View
    entries.forEach(({ word, phonetic, audio }) => {
      const card = document.createElement('div');
      card.classList.add('card');

      const wordEl = document.createElement('div');
      wordEl.classList.add('word');
      wordEl.textContent = word;

      const phoneticEl = document.createElement('div');
      phoneticEl.classList.add('phonetic');
      phoneticEl.textContent = phonetic;

      const audioEl = document.createElement('audio');
      audioEl.src = audio;
      audioEl.classList.add('audio-player');
      audioEl.preload = 'none';
      audioEl.controls = true;
      audioEl.setAttribute('aria-label', `Play audio for word ${word}`);

      card.appendChild(wordEl);
      card.appendChild(phoneticEl);
      card.appendChild(audioEl);
      cardView.appendChild(card);
    });

    let audioElements = [];
    let rowElements = [];
    let currentAudioIndex = 0;
    let isPlaying = false;
    let isPaused = false;
    let showingTable = true; // start with table view

    function setupAudioSequence() {
      // Select audio players only in the visible container
      const container = showingTable ? tableView : cardView;
      audioElements = Array.from(container.querySelectorAll('.audio-player'));
      rowElements = [];

      audioElements.forEach(audio => {
        // Parent row for table, or card div for cards
        const parent = audio.closest('tr') || audio.closest('.card');
        rowElements.push(parent);

        audio.loop = false;
        audio.pause();
        audio.currentTime = 0;

        if (parent) parent.classList.remove('playing');

        audio.onplay = () => {
          audioElements.forEach((a, i) => {
            if (a !== audio) {
              a.pause();
              if (rowElements[i]) rowElements[i].classList.remove('playing');
            }
          });
          if (parent) parent.classList.add('playing');
        };

        audio.onpause = () => {
          if (parent) parent.classList.remove('playing');
        };

        audio.onended = () => {
          if (parent) parent.classList.remove('playing');
          if (isPlaying && !isPaused) {
            const delay = parseInt(document.getElementById('delayInput').value) || 0;
            setTimeout(() => {
              currentAudioIndex = (currentAudioIndex + 1) % audioElements.length;
              playCurrentAudio();
            }, delay);
          }
        };
      });
    }

    function playCurrentAudio() {
      if (audioElements.length === 0) return;
      audioElements.forEach(a => a.pause());
      isPaused = false;
      const currentAudio = audioElements[currentAudioIndex];
      if (currentAudio) currentAudio.play();
    }

    function playAll() {
      if (audioElements.length === 0) return;
      isPlaying = true;
      isPaused = false;
      currentAudioIndex = 0;
      playCurrentAudio();
      playPauseBtn.textContent = '⏸️ Pause';
    }

    function togglePlayPause() {
      if (!isPlaying) return;
      const currentAudio = audioElements[currentAudioIndex];
      if (!currentAudio) return;
      if (isPaused) {
        currentAudio.play();
        isPaused = false;
        playPauseBtn.textContent = '⏸️ Pause';
      } else {
        currentAudio.pause();
        isPaused = true;
        playPauseBtn.textContent = '▶️ Play';
      }
    }

    function toggleLayout() {
      if (showingTable) {
        tableView.style.display = 'none';
        cardView.style.display = 'grid';
        toggleBtn.textContent = 'Table View';
        showingTable = false;
      } else {
        cardView.style.display = 'none';
        tableView.style.display = 'table';
        toggleBtn.textContent = 'Card View';
        showingTable = true;
      }
      isPlaying = false;
      isPaused = false;
      playPauseBtn.textContent = '⏸️ Pause';
      currentAudioIndex = 0;
      setupAudioSequence();
    }

    // Initialize on page load
    document.addEventListener('DOMContentLoaded', () => {
      showingTable = true;
      tableView.style.display = 'table';
      cardView.style.display = 'none';
      toggleBtn.textContent = 'Card View';
      setupAudioSequence();
    });
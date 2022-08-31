# How to generate session/sessionXX.html
1. Create a XX.txt file contains words. For example [session1.txt](https://github.com/chen172/Merriam-Webster-api-example/blob/main/Word%20Power%20Made%20Easy/txt/session1.txt)

2. Run [`ruby pronunciation.rb XX.txt`](https://github.com/chen172/Merriam-Webster-api-example/blob/main/pronunciation.rb) to get needed files, like, prs_session1.txt, [audio_session1.txt](https://github.com/chen172/Merriam-Webster-api-example/blob/main/Word%20Power%20Made%20Easy/txt/prs_session1.txt), and the [audio file](https://github.com/chen172/Merriam-Webster-api-example/tree/main/Word%20Power%20Made%20Easy/audio).

3. Run [`ruby generate_webpage_audio.erb XX.txt`](https://github.com/chen172/Merriam-Webster-api-example/blob/main/generate_webpage_audio.erb) to get the webpage. such as [session1.html](https://github.com/chen172/chen172.github.io/blob/main/session/session1.html)

 async function generate() {
        const inputText = document.getElementById('inputText').value;
        const generatedTextEl = document.getElementById('generatedText');
        const loadingEl = document.getElementById('loading');
        const errorEl = document.getElementById('error');
       
        
        // Reset previous messages
        generatedTextEl.innerText = "";
        errorEl.innerText = "";

        // Show loading message
        loadingEl.style.display = 'block';

        try {
            const response = await fetch('/generate/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: inputText }),
            });

            if (!response.ok) {
                throw new Error('Failed to generate text. Please try again.');
            }

            const data = await response.json();
            generatedTextEl.innerText = data.generated_text || "No text generated.";
        } catch (error) {
            errorEl.innerText = error.message;
        } finally {
            // Hide loading message
            loadingEl.style.display = 'none';
        }
    }

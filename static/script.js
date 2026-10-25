// Find the places where we want to display our topics.
const topicGrid = document.getElementById("topic-grid");
const topicCount = document.getElementById("topic-count");


// Get the topics from our Python backend.
fetch("/api/topics")

    // Convert the response into JavaScript data.
    .then(response => response.json())

    // Display the topics on our webpage.
    .then(topics => {

        // Show the total number of topics.
        topicCount.textContent = topics.length + " Topics";

        // Repeat this code for every topic.
        topics.forEach(topic => {

            // Create a new HTML card.
            const card = document.createElement("article");

            // Give the card its CSS class.
            card.className = "topic-card";

            // Put the topic information inside the card.
            card.innerHTML = `
                <span class="topic-number">
                    TOPIC ${String(topic.id).padStart(2, "0")}
                </span>

                <h3>${topic.title}</h3>

                <span class="topic-link">
                    Explore topic →
                </span>
            `;

            // Put the card on our webpage.
            // Make the card open its topic page when clicked.
            card.addEventListener("click", function() {
                window.location.href = "/topic/" + topic.id;
            });

            // Add the card to the homepage.
            topicGrid.appendChild(card);

        });

    })

    // Show an error in the browser console if something goes wrong.
    .catch(error => {
        console.log("Could not load topics:", error);
        topicCount.textContent = "Unable to load topics";
    });
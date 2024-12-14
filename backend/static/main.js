// JavaScript Functions

async function submitPreferences() {
    const preferences = [];
    ["music", "dance", "podcast"].forEach((id) => {
        if (document.getElementById(id).checked) {
            preferences.push(id);
        }
    });

    const response = await fetch("/api/preferences", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ preferences })
    });

    const data = await response.json();
    if (data.success) {
        window.location.href = "/events";
    }
}

async function fetchEvents() {
    const response = await fetch("/api/events");
    const events = await response.json();

    const list = document.getElementById("eventsList");
    list.innerHTML = "";

    events.forEach((event) => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = `${event.name} - ${event.location} (${event.date})`;
        list.appendChild(li);
    });
}

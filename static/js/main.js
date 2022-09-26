async function getPlayedCharacters(currentActor){
    let data = await fetch (`/get_played_characters?current_actors=${currentActor}`)
    return data.json()
}

async function listCharacters(currentActor) {
    const characters = await getPlayedCharacters(currentActor);
    const actorDiv = document.querySelector('#character')
    actorDiv.innerHTML = ""
    let titleCharacter = document.createElement('h2')
    titleCharacter.textContent = `Played characters by the actor: ${characters[0]['name']}`
    actorDiv.appendChild(titleCharacter)
    for (const character of characters) {
        let paragraph = document.createElement('p')
        paragraph.innerText = character.character_name;
        actorDiv.appendChild(paragraph)
    }
}

function initPage() {
    let actorInTable = document.querySelectorAll('td[data-about-actor]');
    actorInTable.forEach(actor => {
        actor.addEventListener('click', () => {
            const currentActor = actor.dataset.aboutActor
            listCharacters(currentActor)
        })
    })
}

initPage();
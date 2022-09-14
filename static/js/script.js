async function getPlayedCharacters(currentActor){
    let data = await fetch (`/get_played_characters?current_actor=${currentActor}`)
    return data.json()
}

async function listCharacters(currentActor) {
    const characters = await getPlayedCharacters(currentActor);
    const actorDiv = document.querySelector('#character');
    console.log(characters[0]['name'])
    actorDiv.innerHTML = ""
    let titleCharacter = document.createElement('h2')
    titleCharacter.textContent = `Played characters by the actor: ${characters[0]['name']}`
    actorDiv.appendChild(titleCharacter)
    for (const character of characters) {
        let paragraph = document.createElement('p');
        paragraph.innerText = character.character_name;
        // console.log(paragraph)
        actorDiv.appendChild(paragraph)
    }
}

function initPage() {
    // let actorInTable = document.querySelectorAll('[data-set="actors"] tr td')
    let actorInTable = document.querySelectorAll('td[data-about-actor]');
    let clickOnBody = document.querySelector('section');
    // console.log(actorInTable)
    actorInTable.forEach(actor => {
        actor.addEventListener('click', () => {
            console.log(actor.dataset)
            const currentActor = actor.dataset.aboutActor
            listCharacters(currentActor);

        })
    // clickOnBody.addEventListener('click', () => {
    //     let currentActor = 0
    //     listCharacters(currentActor);
    //     })
    })
}

initPage();
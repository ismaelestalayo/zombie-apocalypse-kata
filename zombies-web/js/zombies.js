const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

let scenarioSize = urlParams.get('scenario');
let elementsBase = urlParams.get('elements');
let elements = JSON.parse(elementsBase);




// Absolute positions
let position0 = 0;
let position1 = "80px";
let position2 = "160px";
let position3 = "240px";
let position4 = "320px";
let position5 = "400px";
let position6 = "480px";
let position7 = "560px";
let position8 = "640px";
let position9 = "720px";
let position10 = "800px";
let position11 = "880px";
let position12 = "960px";
let position13 = "1040";
let position14 = "1120";
let position15 = "1200px";


function paintScenario() {
    // Sample de codificador de arrays
    let guardar = [["zombie",0,0],["survivor",2,3],["machete",4,5]];
    var arrStr = encodeURIComponent(JSON.stringify(guardar));
    console.log(arrStr);

    // Display the general scenario
    let tilesQuantity = scenarioSize * scenarioSize;
    let scenarioContainer = document.createElement('div');
    scenarioContainer.setAttribute("id","scenario");
    let scenarioMeasure = scenarioSize * 80;
    scenarioContainer.classList.add("scenario-container");
    scenarioContainer.style.height = scenarioMeasure+"px";
    scenarioContainer.style.width = scenarioMeasure+"px";
    for (var i=0 ; i < tilesQuantity ; i++) {
        let tile = document.createElement("div");
        tile.classList.add("scenario-tile");
        scenarioContainer.appendChild(tile);
    }
    document.body.appendChild(scenarioContainer);

    generateElement();
}



function generateElement() {

    let scenarioReference = document.getElementById("scenario");
    let elementsLenght = elements.length;

    for (var i=0 ; i < elementsLenght ; i++) {
        let innerElement = elements[i];

        let elementClass = innerElement[0];
        let elementPositionX = innerElement[1];
        let elementPositionY = innerElement[2];
        
        let elementContainer = document.createElement('div');
        elementContainer.classList.add("scenario-element");
        if (elementClass == "zombie") { elementContainer.classList.add("type_zombie")}
        else if (elementClass == "survivor") { elementContainer.classList.add("type_survivor")}
        else if (elementClass == "baseballbat") { elementContainer.classList.add("type_bat")}
        else if (elementClass == "rubberduck") { elementContainer.classList.add("type_duck")}
        else if (elementClass == "katana") { elementContainer.classList.add("type_katana")}
        else if (elementClass == "knife") { elementContainer.classList.add("type_knife")}
        else if (elementClass == "handgun") { elementContainer.classList.add("type_handgun")}
        else if (elementClass == "molotov") { elementContainer.classList.add("type_molotov")}
        else if (elementClass == "flamethrower") { elementContainer.classList.add("type_flame")}
        else if (elementClass == "machete") { elementContainer.classList.add("type_machete")}
        else if (elementClass == "bow") { elementContainer.classList.add("type_bow")}

        if (elementPositionX == 0) { elementContainer.style.left = position0}
        else if (elementPositionX == 1) { elementContainer.style.left = position1}
        else if (elementPositionX == 2) { elementContainer.style.left = position2}
        else if (elementPositionX == 3) { elementContainer.style.left = position3}
        else if (elementPositionX == 4) { elementContainer.style.left = position4}
        else if (elementPositionX == 5) { elementContainer.style.left = position5}
        else if (elementPositionX == 6) { elementContainer.style.left = position6}
        else if (elementPositionX == 7) { elementContainer.style.left = position7}
        else if (elementPositionX == 8) { elementContainer.style.left = position8}
        else if (elementPositionX == 9) { elementContainer.style.left = position9}
        else if (elementPositionX == 10) { elementContainer.style.left = position10}
        else if (elementPositionX == 11) { elementContainer.style.left = position11}
        else if (elementPositionX == 12) { elementContainer.style.left = position12}
        else if (elementPositionX == 13) { elementContainer.style.left = position13}
        else if (elementPositionX == 14) { elementContainer.style.left = position14}
        else if (elementPositionX == 15) { elementContainer.style.left = position15}
        
        if (elementPositionY == 0) { elementContainer.style.top = position0}
        else if (elementPositionY == 1) { elementContainer.style.top = position1}
        else if (elementPositionY == 2) { elementContainer.style.top = position2}
        else if (elementPositionY == 3) { elementContainer.style.top = position3}
        else if (elementPositionY == 4) { elementContainer.style.top = position4}
        else if (elementPositionY == 5) { elementContainer.style.top = position5}
        else if (elementPositionY == 6) { elementContainer.style.top = position6}
        else if (elementPositionY == 7) { elementContainer.style.top = position7}
        else if (elementPositionY == 8) { elementContainer.style.top = position8}
        else if (elementPositionY == 9) { elementContainer.style.top = position9}
        else if (elementPositionY == 10) { elementContainer.style.top = position10}
        else if (elementPositionY == 11) { elementContainer.style.top = position11}
        else if (elementPositionY == 12) { elementContainer.style.top = position12}
        else if (elementPositionY == 13) { elementContainer.style.top = position13}
        else if (elementPositionY == 14) { elementContainer.style.top = position14}
        else if (elementPositionY == 15) { elementContainer.style.top = position15}

        scenarioReference.appendChild(elementContainer);
    }
}

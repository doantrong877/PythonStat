
async function get_info(){
    var response = await fetch("https://api.github.com/users/adion81");
    var coderData = await response.json();
    console.log(coderData,"*" * 100, "\n",coderData.followers);
    return coderData
}


function get_something(){
    document.querySelector('h1').innerHTML = "Adrien Dion has "+ get_info().login+ " followers";
}


console.log(get_info());    
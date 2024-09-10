function toggleTopNav() {
    document.getElementById("topDropdown").classList.toggle("show");
    console.log('show')
}

function toggleBotNav() {
    document.getElementById("botDropdown").classList.toggle("show");
    console.log('show')
}
  
// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropdown__target')) {
        var dropdowns = document.getElementsByClassName("dropdown__content");
        if (dropdowns[0].classList.contains('show')){
            dropdowns[0].classList.remove('show')
        }
        console.log('not!')
        console.log(event.target)
    }
}  
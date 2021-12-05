// Start table
let itemMenu = document.getElementById('itemMenu')
let itemColumns = document.getElementById('itemColumns')


itemColumns.onmouseover = function()
{
    itemMenu.style.display = 'block'
}

window.onmouseout = function()
{
    itemMenu.style.display = 'none'
}

// End table
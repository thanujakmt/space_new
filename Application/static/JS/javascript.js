
document.getElementById('menu_list').style.display = 'none';
document.getElementById('close').style.display = 'none';
document.getElementById('menu').style.display = 'flex';

var menu_btn = document.getElementById('menu');

menu_btn.addEventListener('click', () =>{
    document.getElementById('menu_list').style.display = 'block';
    document.getElementById('close').style.display = 'block';
    document.getElementById('menu').style.display = 'none';
});

var close_btn = document.getElementById('close');

close_btn.addEventListener('click', () => {
    document.getElementById('menu_list').style.display = 'none';
    document.getElementById('close').style.display = 'none';
    document.getElementById('menu').style.display = 'block';
});
let update_time = new Date('2025/02/21 23:57');
update_time.setHours(update_time.getHours() + 9);
document.getElementById('last_update').innerText = update_time.toLocaleString().slice(0,-3);

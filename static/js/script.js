const deleteButton = document.getElementById('delete');

// Event listeners for SweetAlerts defensive design

if (deleteButton) {
    deleteButton.addEventListener('click', confirmDelete);
}

/** Get href url of button delete.
*/
function goToDeleteUrl() {
    let href = document.getElementById('delete').getAttribute('href');
    window.location.href = `${href}`;
}

/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect to /delete/{{ project.id }}
*/
function confirmDelete(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure you want to delete your profile?',
        text: 
        "This action is non-reversible. You will loose all of your data and conversations with your advisor!",
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--fuzzy-wuzzy)',
        cancelButtonColor: 'var(--liberty)',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToDeleteUrl();
        }
    });
}
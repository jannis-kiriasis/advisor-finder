const deleteButton = document.getElementById('delete');
const updateAdvisorButton = document.getElementById('update_advisor');
const updateSeekerButton = document.getElementById('update_seeker');


// Event listeners for SweetAlerts defensive design
if (deleteButton) {
    deleteButton.addEventListener('click', confirmDelete);
}

if (updateAdvisorButton) {
    updateAdvisorButton.addEventListener('click', confirmUpdateAdvisor);
}

if (updateSeekerButton) {
    updateSeekerButton.addEventListener('click', confirmUpdateSeeker);
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


/** Get href url of button update advisor.
*/
function goToUpdateUrlAdvisor() {
    let href = document.getElementById('update_advisor').getAttribute(
        'href');
    window.location.href = `${href}`;
}


/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect.
*/
function confirmUpdateAdvisor(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure you want to update your profile?',
        text: 
        "Your profile will be sent to Advice Found for approval. You won't be able to receive new clients while your profile in under review.",
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--verdigris)',
        cancelButtonColor: 'var(--fuzzy-wuzzy)',
        confirmButtonText: 'Yes, update it!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToUpdateUrlAdvisor();
        }
    });
}


/** Get href url of button update seeker.
*/
function goToUpdateUrlSeeker() {
    let href = document.getElementById('update_seeker').getAttribute(
        'href');
    window.location.href = `${href}`;
}


/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect.
*/
function confirmUpdateSeeker(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure you want to update you profile?',
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--verdigris)',
        cancelButtonColor: 'var(--fuzzy-wuzzy)',
        confirmButtonText: 'Yes, update it!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToUpdateUrlSeeker();
        }
    });
}
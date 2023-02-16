const deleteButton = document.getElementById('delete');
const updateAdvisorButton = document.getElementById('update_advisor');
const updateSeekerButton = document.getElementById('update_seeker');
const deactivateButton = document.getElementById('deactivate_advisor');

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

if (deactivateButton) {
    deactivateButton.addEventListener('click', deactivateAdvisorChoice);
}

/** Get href url of button delete.
*/
function goToDeleteUrl() {
    let href = document.getElementById('delete').getAttribute('href');
    window.location.href = `${href}`;
}


/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect.
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


/** Get href url of deactivate button.
*/
function goToDeactivateAdvisor() {
    let href = document.getElementById('deactivate_advisor').getAttribute(
        'href');
    window.location.href = `${href}`;
}


/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect.
*/
function deactivateAdvisor(event) {
    event.preventDefault();

    Swal.fire({
        title: 'Are you sure you want to deactivate you profile?',
        text: 'You will be hidden and not assigned new leads.',
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--verdigris)',
        cancelButtonColor: 'var(--fuzzy-wuzzy)',
        confirmButtonText: 'Yes, deactivate me!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToDeactivateAdvisor();
        }
    })
}


function activateAdvisor(event) {
    event.preventDefault();

    Swal.fire({
        title: 'Are you sure you want to activate you profile?',
        text: 'You will be visible and will start to receive new leads.',
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--verdigris)',
        cancelButtonColor: 'var(--fuzzy-wuzzy)',
        confirmButtonText: 'Yes, activate me!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToDeactivateAdvisor();
        }
    });  
}


/** For deactivate_advisor button:
 * if button text is Deactivate profile call deativate function 
 * else call activate.
*/
function deactivateAdvisorChoice(event) {

    if (deactivateButton.text === 'Deactivate profile') {
        deactivateAdvisor(event);
    } else if (deactivateButton.text === 'Activate profile') {
        activateAdvisor(event);
    }

}

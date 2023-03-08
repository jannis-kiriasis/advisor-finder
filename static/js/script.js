const deleteButton = document.getElementById('delete');
const updateAdvisorButton = document.getElementById('update_advisor');
const updateSeekerButton = document.getElementById('update_seeker');
const deactivateButton = document.getElementById('deactivate_advisor');
const chooseAdvisorButton = document.getElementsByClassName('advisor');

let alert = document.getElementsByClassName('alert')[0];

// Remove alert box after 5 seconds
if (alert) {
    setTimeout(() => {
        alert.classList.remove('show')
        alert.addClass('hide')
    }, 5000)
}

// Event listeners for SweetAlerts defensive design
if (deleteButton) {
    deleteButton.addEventListener('click', confirmDelete);
}

// if (updateAdvisorButton) {
//     updateAdvisorButton.addEventListener('click', confirmUpdateAdvisor);
// }

if (updateSeekerButton) {
    updateSeekerButton.addEventListener('click', confirmUpdateSeeker);
}

// if (deactivateButton) {
//     deactivateButton.addEventListener('click', deactivateAdvisorChoice);
// }

if (chooseAdvisorButton) {
    for (var i = 0 ; i < chooseAdvisorButton.length; i++) {
        chooseAdvisorButton[i].addEventListener('click' , messageAdvisor) ; 
     }
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
        confirmButtonColor: 'var(--brown)',
        cancelButtonColor: 'var(--sapphire)',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToDeleteUrl();
        }
    });
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
        confirmButtonColor: 'var(--dark-verdigris)',
        cancelButtonColor: 'var(--brown)',
        confirmButtonText: 'Yes, update it!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.reload();
        }
    });
}

/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect.
*/
function confirmUpdateSeeker(event) {
    event.preventDefault();

    var saveNeed = $("#id_need :selected").text();
    var savePostcode = $('#id_postcode').attr('value');
    var saveTownOrCity = $('#id_town_or_city :selected').text();
    var saveStreetAddress = $('#id_street_address').attr('value');
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'save_need': saveNeed,
        'save_postcode': savePostcode,
        'save_town_or_city': saveTownOrCity,
        'save_street_address': saveStreetAddress,
    };
    var url = document.getElementById('update_seeker').getAttribute(
        'data-url');;

    Swal.fire({
        title: 'Are you sure you want to update you profile?',
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--dark-verdigris)',
        cancelButtonColor: 'var(--brown)',
        confirmButtonText: 'Yes, update it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.post(url, postData);
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
        confirmButtonColor: 'var(--dark-verdigris)',
        cancelButtonColor: 'var(--brown)',
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
        confirmButtonColor: 'var(--dark-verdigris)',
        cancelButtonColor: 'var(--brown)',
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


/** Fire alert before to message advisor for the first time.
*/
function messageAdvisor(event) {
    event.preventDefault();

    Swal.fire({
        title: 'Ready to chat?',
        text: "You'll be assigned to this advisor. Should you wish to change advisor in the future please contact jannis.kiriasis@gmail.com",
        icon: 'info',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--dark-verdigris)',
        cancelButtonColor: 'var(--brown)',
        confirmButtonText: 'Yes, start chat!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = event.target.href
        }
    });  
}



const deleteButton = document.getElementById('delete');
const deleteAppointmentButton = document.getElementsByClassName(
    'delete-appointment');
const updateAdvisorButton = document.getElementById('update_advisor');
const updateSeekerButton = document.getElementById('update_seeker');
const deactivateButton = document.getElementById('deactivate_advisor');
const chooseAdvisorButton = document.getElementsByClassName('advisor');

// Get alert box
const alert = document.getElementsByClassName('alert')[0];
const alertTwo = document.getElementsByClassName('alert')[1];
// Make alert box disappear after 5 seconds
if (alert) {
    setTimeout(function() {
        alert.classList.remove('show');
    }, 5000);
}

if (alertTwo) {
    setTimeout(function() {
        alertTwo.classList.remove('show');
    }, 5000);
}

// Event listeners for SweetAlerts defensive design
if (deleteButton) {
    deleteButton.addEventListener('click', confirmDelete);
}

if (deleteAppointmentButton) {
    for (var i = 0 ; i < deleteAppointmentButton.length; i++) {
        deleteAppointmentButton[i].addEventListener(
            'click', confirmDeleteAppointment);
    }
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

if (chooseAdvisorButton) {
    for (var i = 0 ; i < chooseAdvisorButton.length; i++) {
        chooseAdvisorButton[i].addEventListener('click' , messageAdvisor) ; 
     }
}

/** Defensive design for delete seeker button.
*/
function confirmDelete(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure you want to delete your profile?',
        text: 
        "This action is non-reversible. You will loose all of your data and conversations with your advisor!",
        icon: 'warning',
        iconColor: 'var(--ecru)',
        showCancelButton: true,
        confirmButtonColor: 'var(--brown)',
        cancelButtonColor: 'var(--cobalt)',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
                window.location.href = event.target.href;
            }
    });
}

/** Defensive design for delete appointment button.
*/
function confirmDeleteAppointment(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure you want to delete this consultation?',
        text: 
        "This action is non-reversible. You'll have to reschedule one if needed.",
        icon: 'warning',
        iconColor: 'var(--ecru)',
        showCancelButton: true,
        confirmButtonColor: 'var(--brown)',
        cancelButtonColor: 'var(--cobalt)',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
                window.location.href = event.target.href;
            }
    });
}

/** Save advisor details, fire defensive design
 * and post the advisor details to the update advisor view.
*/
function confirmUpdateAdvisor(event) {
    event.preventDefault();

    var saveSpecialisation = $("#id_specialisation :selected").text();
    var savePostcode = $('#id_postcode').val();
    var saveBusinessName = $('#id_business_name').val();
    var saveBusinessDescription = $('#id_business_description').text();
    var saveRegistrationNumber = $('#id_registration_number').val();
    var saveTownOrCity = $('#id_town_or_city :selected').text();
    var saveStreetAddress = $('#id_street_address').val();
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'save_specialisation': saveSpecialisation,
        'save_business_name': saveBusinessName,
        'save_business_description': saveBusinessDescription,
        'save_registration_number': saveRegistrationNumber,
        'save_postcode': savePostcode,
        'save_town_or_city': saveTownOrCity,
        'save_street_address': saveStreetAddress,
    };

    var url = document.getElementById('update_advisor').getAttribute(
        'data-url');

    Swal.fire({
        title: 'Are you sure you want to update your profile?',
        text: 
        "Your profile will be sent to Advice Found for approval. You won't be able to receive new clients while your profile in under review.",
        icon: 'warning',
        iconColor: 'var(--ecru)',
        showCancelButton: true,
        confirmButtonColor: 'var(--caribbean-current)',
        cancelButtonColor: 'var(--brown)',
        confirmButtonText: 'Yes, update it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.post(url, postData).done(function(){
            }).fail(function () {
                // just reload the page, the error will be in django messages
                location.reload();
            });
        }
    });
}

/** Save seeker details, fire defensive design
 * and post the seeker details to the update seeker view.
*/
function confirmUpdateSeeker(event) {
    event.preventDefault();

    var saveNeed = $("#id_need :selected").text();
    var savePostcode = $('#id_postcode').val();
    var saveTownOrCity = $('#id_town_or_city :selected').text();
    var saveStreetAddress = $('#id_street_address').val();
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
        'data-url');

    Swal.fire({
        title: 'Are you sure you want to update you profile?',
        icon: 'warning',
        iconColor: 'var(--ecru)',
        showCancelButton: true,
        confirmButtonColor: 'var(--caribbean-current)',
        cancelButtonColor: 'var(--brown)',
        confirmButtonText: 'Yes, update it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.post(url, postData).done(function(){
            }).fail(function () {
                // just reload the page, the error will be in django messages
                location.reload();
            });
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

/** Defensive design for deactivate advisor profile button
*/
function deactivateAdvisor(event) {
    event.preventDefault();

    Swal.fire({
        title: 'Are you sure you want to deactivate you profile?',
        text: 'You will be hidden and not assigned new leads.',
        icon: 'warning',
        iconColor: 'var(--ecru)',
        showCancelButton: true,
        confirmButtonColor: 'var(--caribbean-current)',
        cancelButtonColor: 'var(--brown)',
        confirmButtonText: 'Yes, deactivate me!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToDeactivateAdvisor();
        }
    });
}

/** Defensive design for activate advisor profile button
*/
function activateAdvisor(event) {
    event.preventDefault();

    Swal.fire({
        title: 'Are you sure you want to activate you profile?',
        text: 'You will be visible and will start to receive new leads.',
        icon: 'warning',
        iconColor: 'var(--ecru)',
        showCancelButton: true,
        confirmButtonColor: 'var(--caribbean-current)',
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
        iconColor: 'var(--ecru)',
        showCancelButton: true,
        confirmButtonColor: 'var(--caribbean-current)',
        cancelButtonColor: 'var(--brown)',
        confirmButtonText: 'Yes, start chat!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = event.target.href;
        }
    });  
}
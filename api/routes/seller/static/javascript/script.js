const slider = document.getElementById('compression-ratio');
const output = document.getElementById('output-ratio');

slider.addEventListener('input', function () {
  output.textContent = slider.value;
});

function validateForm () {
  const fileInput = document.getElementById('fileUpload');
  const errorMessage = document.getElementById('error-message');

  if (!fileInput.files || fileInput.files.length === 0) {
    errorMessage.textContent = 'Please select a file to upload.';
    return false; // Prevent form submission
  }

  errorMessage.textContent = ''; // Clear error message if valid
  return true; // Allow form submission
}

// Webcam capture functionality
function captureWebcam() {
    const video = document.getElementById('videoElement');
    const videoPreview = document.getElementById('videoPreview');
    
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                video.srcObject = stream;
                video.style.display = "block";
                videoPreview.style.display = "none";
            })
            .catch(function (err0r) {
                alert("Webcam access denied or not available.");
            });
    }
}

// Function to send captured image to Python backend
function sendImageToPython(imageData) {
    fetch('/process-image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: imageData }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from Python backend
        updateUIWithResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing the image.');
    });
}

// Function to update UI with results from Python backend
function updateUIWithResults(data) {
    document.getElementById('detectedAmount').textContent = `$${data.amount.toFixed(2)}`;
    document.getElementById('invoiceCategory').textContent = data.category;
    document.getElementById('invoiceDate').textContent = data.date;
    document.getElementById('invoiceVendor').textContent = data.vendor;
    document.getElementById('invoiceItems').textContent = data.items.join(', ');
}

// Modify captureWebcam function to send image to Python backend
function captureWebcam() {
    const video = document.getElementById('videoElement');
    const videoPreview = document.getElementById('videoPreview');
    
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                video.srcObject = stream;
                video.style.display = "block";
                videoPreview.style.display = "none";
                
                // Capture image after a short delay
                setTimeout(() => {
                    const canvas = document.createElement('canvas');
                    canvas.width = video.videoWidth;
                    canvas.height = video.videoHeight;
                    canvas.getContext('2d').drawImage(video, 0, 0);
                    const imageData = canvas.toDataURL('image/jpeg');
                    sendImageToPython(imageData);
                    
                    // Stop the video stream
                    stream.getTracks().forEach(track => track.stop());
                }, 1000); // Adjust delay as needed
            })
            .catch(function (error) {
                alert("Webcam access denied or not available.");
            });
    }
}

// File upload trigger
function triggerUpload() {
    document.getElementById('fileInput').accept = "video/*";
    document.getElementById('fileInput').click();
}

function triggerImageUpload() {
    document.getElementById('fileInput').accept = "image/*";
    document.getElementById('fileInput').click();
}
// Handle file upload
function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const fileType = file.type.split('/')[0];
        if (fileType === 'video' || fileType === 'image') {
            document.getElementById('uploadOverlay').style.display = 'none';
            simulateUploadAndProcess();
            
            if (fileType === 'image') {
                displayUploadedImage(file);
            } else {
                displayUploadedVideo(file);
            }
        } else {
            alert('Please upload a valid video or image file.');
        }
    }
}

function uploadAndProcessFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    fetch('/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Processing result:', data);
        updateInvoiceDetails(data);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing the file.');
    });

    simulateUploadAndProcess();
}

function updateInvoiceDetails(data) {
    // Update this function to display the processed data from the Python script
    document.getElementById('invoiceNumber').textContent = data.details.type;
    document.getElementById('invoiceDate').textContent = data.details.size;
    document.getElementById('totalAmount').textContent = data.message;
}
function displayUploadedImage(file) {
    const videoPreview = document.getElementById('videoPreview');
    const img = document.createElement('img');
    img.src = URL.createObjectURL(file);
    img.style.maxWidth = '100%';
    img.style.maxHeight = '100%';
    videoPreview.innerHTML = '';
    videoPreview.appendChild(img);
}
function displayUploadedVideo(file) {
    const videoElement = document.getElementById('videoElement');
    videoElement.src = URL.createObjectURL(file);
    videoElement.style.display = 'block';
    document.querySelector('#videoPreview p').style.display = 'none';
}

// Show/Hide upload overlay
function showUploadOverlay(show) {
    const uploadOverlay = document.getElementById('uploadOverlay');
    uploadOverlay.classList.toggle('active', show);
}

// Simulate file upload and invoice processing
function simulateUploadAndProcess() {
    const progressBar = document.getElementById('progress');
    const processingStatus = document.getElementById('processingStatus');

    let progress = 0;
    const interval = setInterval(() => {
        if (progress < 100) {
            progress += 10;
            progressBar.style.width = progress + '%';
            processingStatus.innerText = `Processing: ${progress}%`;
        } else {
            clearInterval(interval);
            processingStatus.innerText = "Invoice processed successfully!";
            updateInvoiceDetails();
        }
    }, 300);
}

// Simulate invoice data extraction and update the UI
function updateInvoiceDetails() {
    const detectedAmount = document.getElementById('detectedAmount');
    const invoiceCategory = document.getElementById('invoiceCategory');
    const invoiceDate = document.getElementById('invoiceDate');
    const invoiceVendor = document.getElementById('invoiceVendor');
    const invoiceItems = document.getElementById('invoiceItems');

    // Simulated data
    detectedAmount.innerText = "Rs.1,250.50";
    invoiceCategory.innerText = "Office Supplies";
    invoiceDate.innerText = "2024-09-15";
    invoiceVendor.innerText = "ACME Corp";
    invoiceItems.innerText = "23 items";
}

// Export data functionality
function exportData() {
    alert("Exported data successfully!");
}
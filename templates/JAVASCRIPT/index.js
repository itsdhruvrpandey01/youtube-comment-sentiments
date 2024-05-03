// JavaScript function to handle hovering effect
        function handleHover(element) {
            if (element.style.backgroundColor === "") {
                element.style.backgroundColor = "lightblue";
            } else {
                element.style.backgroundColor = "";
            }
        }

        // JavaScript function to open the modal
        function openModal() {
            var modal = document.getElementById('myModal');
            modal.style.display = "block";
            
            // Render chart when modal opens
            var chart = new CanvasJS.Chart("chartContainer", {
                animationEnabled: true,
                title: {
                    text: "Sentiment Analysis Result."
                },
                data: [{
                    type: "pie",
                    startAngle: 240,
                    yValueFormatString: "##0.00\"%\"",
                    indexLabel: "{label} {y}",
                    dataPoints: [
                        {y: parseInt(document.getElementById('positive-count').textContent), label: "Positive"},
                        {y: parseInt(document.getElementById('negative-count').textContent), label: "Negative"},
                        {y: parseInt(document.getElementById('neutral-count').textContent), label: "Neutral"},
                        {y: parseInt(document.getElementById('unidentified-count').textContent), label: "Undefined"}
                    ]
                }]
            });
            chart.render();
        }

        // JavaScript function to close the modal
        function closeModal() {
            var modal = document.getElementById('myModal');
            modal.style.display = "none";
        }

        // JavaScript function for filtering the comments based on the sentiments
        function filterComments(sentiment) {
            var rows = document.querySelectorAll('tbody tr');
            rows.forEach(function(row) {
                var rowSentiment = row.lastElementChild.textContent.trim();
                if (sentiment === 'all' || rowSentiment === sentiment) {
                    row.style.display = 'table-row';
                } else {
                    row.style.display = 'none';
                }
            });
        }

        // JavaScript function to toggle dark mode
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
            var darkModeButton = document.getElementById('dark-mode-button');
            if (document.body.classList.contains('dark-mode')) {
                darkModeButton.innerHTML = '<i class="fas fa-sun"></i>';
            } else {
                darkModeButton.innerHTML = '<i class="fas fa-moon"></i>';
            }
        }

        window.onload = function() {
            var totalComments = parseInt(document.getElementById('positive-count').textContent) +
                parseInt(document.getElementById('negative-count').textContent) +
                parseInt(document.getElementById('neutral-count').textContent) +
                parseInt(document.getElementById('unidentified-count').textContent)

            // Update total count in HTML
            document.getElementById('total-count').textContent = totalComments;

            var buttons = document.querySelectorAll('.btnSize');
            var maxWidth = 0;

            // Find the maximum width among all buttons
            buttons.forEach(function(button) {
                var buttonWidth = button.offsetWidth;
                if (buttonWidth > maxWidth) {
                    maxWidth = buttonWidth;
                }
            });

            // Set the width of all buttons to the maximum width
            buttons.forEach(function(button) {
                button.style.width = maxWidth + 'px';
            });

            // Check if the user prefers dark mode
            if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                toggleDarkMode();
            }
        };

 // Function to generate a random math problem and set it in the HTML
        function generateMathProblem() {
            const operand1 = Math.floor(Math.random() * 10) + 1;
            const operand2 = Math.floor(Math.random() * 10) + 1;
            document.getElementById('mathProblem').textContent = `${operand1} + ${operand2}`;
        }

        // Function to create account (placeholder function for demonstration)
        function createAccount() {
            // You can replace this function with your actual account creation logic
            alert('Account created successfully!');
        }

        // Initialize the form with a random math problem
        generateMathProblem();
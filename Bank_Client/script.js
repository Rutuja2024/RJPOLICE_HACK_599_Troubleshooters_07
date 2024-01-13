
function openTransactionsForm() {
    // Open a new window or tab with the form
    const transactionsFormWindow = window.open('transactions.html', '_blank');
    // You can customize the window features if needed
    // Example: window.open('transactions.html', '_blank', 'width=600,height=400');
}

function handleOption(option) {
    let resultMessage = "";

    switch (option) {
        case 'transactions':
            break;
        case 'form-transact':
            const trans = window.open('transactions.html', '_blank');
            return; 
        case 'account':
            const acc = window.open('account.html', '_blank');
            return; 
        default:
            break;
    }

    document.getElementById('actionResult').innerText = resultMessage;
}


function searchTable() {
    const input = document.getElementById('searchInput');
    const filter = input.value.toUpperCase();
    const table = document.querySelector('table');
    const rows = table.querySelectorAll('tbody tr');
    let found = false;

    rows.forEach(row => {
        const dataA = row.querySelector('td:nth-child(1)').textContent.toUpperCase();
        if (dataA.includes(filter)) {
            row.style.display = '';
            found = true;
        } else {
            row.style.display = 'none';
        }
    });

    const noResultsMessage = document.getElementById('noResultsMessage');
    if (found) {
        noResultsMessage.style.display = 'none';
    } else {
        noResultsMessage.style.display = 'block';
    }
}
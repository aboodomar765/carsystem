// Search and Filter
function applyFilters() {
    const searchInput = document.getElementById('searchInput');
    const statusFilter = document.getElementById('statusFilter');
    
    if (searchInput && statusFilter) {
        const search = searchInput.value;
        const status = statusFilter.value;
        const url = new URL(window.location);
        
        if (search) {
            url.searchParams.set('search', search);
        } else {
            url.searchParams.delete('search');
        }
        
        if (status) {
            url.searchParams.set('status', status);
        } else {
            url.searchParams.delete('status');
        }
        
        window.location.href = url.toString();
    }
}

// Delete confirmation
function confirmDelete(message) {
    return confirm(message || 'هل أنت متأكد من الحذف؟');
}

// Date range filter
function applyDateFilter() {
    const startDate = document.getElementById('startDate');
    const endDate = document.getElementById('endDate');
    
    if (startDate && endDate) {
        const url = new URL(window.location);
        
        if (startDate.value) {
            url.searchParams.set('start_date', startDate.value);
        }
        if (endDate.value) {
            url.searchParams.set('end_date', endDate.value);
        }
        
        window.location.href = url.toString();
    }
}

// Clear filters
function clearFilters() {
    window.location.href = window.location.pathname;
}

// Format currency
function formatCurrency(value) {
    return new Intl.NumberFormat('ar-SA', {
        style: 'currency',
        currency: 'SAR'
    }).format(value);
}

// Format date
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('ar-SA', options);
}

// Initialize tooltips
function initializeTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    tooltips.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.getAttribute('data-tooltip');
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.position = 'fixed';
            tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
            tooltip.style.left = rect.left + 'px';
        });
    });
}

// Document ready
document.addEventListener('DOMContentLoaded', function() {
    initializeTooltips();
    
    // Search input enter key
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                applyFilters();
            }
        });
    }
});

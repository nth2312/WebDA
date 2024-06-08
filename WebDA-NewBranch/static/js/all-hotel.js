const showHotel = (hotel) => `
<div class="strip_all_tour_list wow fadeIn" data-wow-delay="0.1s" style="border-radius: 10px; overflow: hidden;">
    <div class="row">
        <div class="col-lg-4 col-md-4 col-sm-4">
            <div class="img_list">
                <a href="/hdetail/${hotel.hotel_name}">
                    <img alt="${hotel.hotel_name}" class="attachment-330x220 size-330x220 wp-post-image" height="220"
                        loading="lazy" sizes="(max-width: 330px) 100vw, 330px"
                        src="/static/images/hotel/${hotel.hotel_name}.jpg"
                    </img>
                </a>
            </div>
        </div>
        <div class="clearfix visible-xs-block"></div>
        <div class="col-lg-6 col-md-6 col-sm-6">
            <div class="tour_list_desc">
                <div class="rating">
                    <i class="icon-star voted"></i><i class="icon-star voted"></i><i class="icon-star voted"></i><i class="icon-star voted"></i><i class="icon-star-empty"></i>
                </div>
                <h3 style="font-weight: bold">${hotel.hotel_name}</h3>
                <p style="font-size: 20px;">${hotel.hotel_short}</p>
            </div>
        </div>
        <div class="col-lg-2 col-md-2 col-sm-2">
            <div class="price_list">
                <div>
                    <span>${hotel.hotel_averagePrice}<sup>đ</sup></span> 
                    <p><a class="btn_1" href="/hdetail/${hotel.hotel_name}">Chi tiết</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
`;

const showFixedHotels = (hotels) => {
    const tourListContainer = document.getElementById('hotel-container');
    tourListContainer.classList.add('show-fade-out');
    setTimeout(() => {
        tourListContainer.innerHTML = hotels.map(showHotel).join('');
        tourListContainer.classList.remove('show-fade-out');
        tourListContainer.classList.add('show-fade-in');
        setTimeout(() => {
            tourListContainer.classList.remove('show-fade-in');
        }, 500);
    }, 500);
};

const loadAllHotels = async () => {
    try {
        const response = await fetch('/GetAllInfor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ type: 'hotel' })
        });
        const hotels = await response.json();
        showFixedHotels(hotels);
    } catch (error) {
        console.error('Error fetching hotels:', error);
    }
};

const loadFilteredHotels = async () => {
    const selectedRadio = document.querySelector('input[name="price_filter[]"]:checked');
    let inputLabelText = '';
    if (selectedRadio) {
        const label = selectedRadio.parentElement;
        inputLabelText = label.textContent.trim();
    }
    const type = 'hotel';
    try {
        const response = await fetch('/GetFilteredInfor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ inputLabelText, type })
        });
        const hotels = await response.json();
        if (hotels.status !== "none") {
            showFixedHotels(hotels);
        } else {
            const hotelContainer = document.getElementById('hotel-container');
            hotelContainer.classList.add('show-fade-out');
            setTimeout(() => {
                hotelContainer.innerHTML = "Không có khách sạn nào phù hợp!";
                hotelContainer.classList.remove('show-fade-out');
                hotelContainer.classList.add('show-fade-in');
                setTimeout(() => {
                    hotelContainer.classList.remove('show-fade-in');
                }, 500);
            }, 500);
        }
    } catch (error) {
        console.error('Error fetching filtered hotels:', error);
    }
};

document.addEventListener('DOMContentLoaded', () => loadAllHotels());
document.getElementById('search-button').addEventListener('click', () => {
    loadFilteredHotels();
});

function formatPrice(price){
    if (price === 0) {
        return "miễn phí";
    }
    return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") + "<sup>đ</sup> ";
}

const showPlace = (place) => `
<div class="strip_all_tour_list wow fadeIn" data-wow-delay="0.1s" style="border-radius: 10px; overflow: hidden;">
    <div class="row">
        <div class="col-lg-4 col-md-4 col-sm-4">
            <div class="img_list">
                <a href="/pdetail/${place.place_name}">
                    <img alt="${place.place_name}" class="attachment-330x220 size-330x220 wp-post-image" height="220"
                        loading="lazy" sizes="(max-width: 330px) 100vw, 330px"
                        src="/static/images/place/${place.place_id}.jpg"
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
                <h3 style="font-weight: bold">${place.place_name}</h3>
                <p style="font-size: 20px;">${place.place_short}</p>
            </div>
        </div>
        <div class="col-lg-2 col-md-2 col-sm-2">
            <div class="price_list">
                <div>
<<<<<<< HEAD
                    <span id="price">${place.place_entryPrice}<sup>đ</sup></span>
=======
                    <span id="price">${formatPrice(place.place_entryPrice)}</span>
>>>>>>> c5e8286b3aa34635b412ad07d0a516623dce8304
                    <p><a class="btn_1" href="/pdetail/${place.place_name}">Chi tiết</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
`;

const showFixedPlaces = (places) => {
    const tourListContainer = document.getElementById('place-container');
    tourListContainer.classList.add('show-fade-out');
    setTimeout(() => {
        tourListContainer.innerHTML = places.map(showPlace).join('');
        tourListContainer.classList.remove('show-fade-out');
        tourListContainer.classList.add('show-fade-in');
        setTimeout(() => {
            tourListContainer.classList.remove('show-fade-in');
        }, 500);
    }, 500);
};

const loadAllPlaces = async () => {
    try {
        const response = await fetch('/GetAllInfor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ type: 'place' })
        });
        const places = await response.json();
        showFixedPlaces(places);
    } catch (error) {
        console.error('Error fetching places:', error);
    }
};

const loadFilteredPlaces = async () => {
    const selectedRadio = document.querySelector('input[name="price_filter[]"]:checked');
    let inputLabelText = '';
    if (selectedRadio) {
        const label = selectedRadio.parentElement;
        inputLabelText = label.textContent.trim();
    }
    const type = 'place';
    try {
        const response = await fetch('/GetFilteredInfor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ inputLabelText, type })
        });
        const places = await response.json();
        if (places.status !== "none") {
            showFixedPlaces(places);
        } else {
            const placeContainer = document.getElementById('place-container');
            placeContainer.classList.add('show-fade-out');
            setTimeout(() => {
                placeContainer.innerHTML = "Không có địa điểm nào phù hợp!";
                placeContainer.classList.remove('show-fade-out');
                placeContainer.classList.add('show-fade-in');
                setTimeout(() => {
                    placeContainer.classList.remove('show-fade-in');
                }, 500);
            }, 500);
        }
    } catch (error) {
        console.error('Error fetching filtered places:', error);
    }
};

document.addEventListener('DOMContentLoaded', () => loadAllPlaces());
document.getElementById('search-button').addEventListener('click', () => {
    loadFilteredPlaces();
});

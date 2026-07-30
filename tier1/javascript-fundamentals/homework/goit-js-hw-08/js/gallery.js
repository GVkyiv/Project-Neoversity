const images = [
  {
    preview:
      'https://cdn.pixabay.com/photo/2019/05/14/16/43/rchids-4202820__480.jpg',
    original:
      'https://cdn.pixabay.com/photo/2019/05/14/16/43/rchids-4202820_1280.jpg',
    description: 'Hokkaido Flower',
  },
  {
    preview:
      'https://cdn.pixabay.com/photo/2019/05/14/22/05/container-4203677__340.jpg',
    original:
      'https://cdn.pixabay.com/photo/2019/05/14/22/05/container-4203677_1280.jpg',
    description: 'Container Haulage Freight',
  },
  {
    preview:
      'https://cdn.pixabay.com/photo/2019/05/16/09/47/beach-4206785__340.jpg',
    original:
      'https://cdn.pixabay.com/photo/2019/05/16/09/47/beach-4206785_1280.jpg',
    description: 'Aerial Beach View',
  },
  {
    preview:
      'https://cdn.pixabay.com/photo/2016/11/18/16/19/flowers-1835619__340.jpg',
    original:
      'https://cdn.pixabay.com/photo/2016/11/18/16/19/flowers-1835619_1280.jpg',
    description: 'Flower Blooms',
  },
  {
    preview:
      'https://cdn.pixabay.com/photo/2018/09/13/10/36/mountains-3674334__340.jpg',
    original:
      'https://cdn.pixabay.com/photo/2018/09/13/10/36/mountains-3674334_1280.jpg',
    description: 'Alpine Mountains',
  },
  {
    preview:
      'https://cdn.pixabay.com/photo/2019/05/16/23/04/landscape-4208571__340.jpg',
    original:
      'https://cdn.pixabay.com/photo/2019/05/16/23/04/landscape-4208571_1280.jpg',
    description: 'Mountain Lake Sailing',
  },
  {
    preview:
      'https://cdn.pixabay.com/photo/2019/05/17/09/27/the-alps-4209272__340.jpg',
    original:
      'https://cdn.pixabay.com/photo/2019/05/17/09/27/the-alps-4209272_1280.jpg',
    description: 'Alpine Spring Meadows',
  },
  {
    preview:
      'https://cdn.pixabay.com/photo/2019/05/16/21/10/landscape-4208255__340.jpg',
    original:
      'https://cdn.pixabay.com/photo/2019/05/16/21/10/landscape-4208255_1280.jpg',
    description: 'Nature Landscape',
  },
  {
    preview:
      'https://cdn.pixabay.com/photo/2019/05/17/04/35/lighthouse-4208843__340.jpg',
    original:
      'https://cdn.pixabay.com/photo/2019/05/17/04/35/lighthouse-4208843_1280.jpg',
    description: 'Lighthouse Coast Sea',
  },
];

const gallery = document.querySelector('.gallery');

const galleryMarkup = images
  .map(
    ({ preview, original, description }) => `
      <li class="gallery-item">
        <a class="gallery-link" href="${original}">
          <img
            class="gallery-image"
            src="${preview}"
            data-source="${original}"
            alt="${description}"
          />
        </a>
      </li>
    `
  )
  .join('');

gallery.innerHTML = galleryMarkup;

gallery.addEventListener('click', onGalleryClick);

let currentImageIndex = 0;

function onGalleryClick(event) {
  event.preventDefault();

  const galleryImage = event.target;

  if (!galleryImage.classList.contains('gallery-image')) {
    return;
  }

  const largeImageUrl = galleryImage.dataset.source;
  const imageDescription = galleryImage.alt;
  currentImageIndex = images.findIndex(({ original }) => original === largeImageUrl);

  const instance = basicLightbox.create(`
    <div class="modal-gallery">
      <button class="modal-button modal-button-prev" type="button" aria-label="Previous image">
        &#10094;
      </button>
      <img
        class="modal-image"
        src="${largeImageUrl}"
        alt="${imageDescription}"
      />
      <button class="modal-button modal-button-next" type="button" aria-label="Next image">
        &#10095;
      </button>
    </div>
  `);

  instance.show();

  const modal = instance.element();
  const modalImage = modal.querySelector('.modal-image');
  const prevButton = modal.querySelector('.modal-button-prev');
  const nextButton = modal.querySelector('.modal-button-next');

  prevButton.addEventListener('click', () => {
    currentImageIndex =
      (currentImageIndex - 1 + images.length) % images.length;
    updateModalImage(modalImage);
  });

  nextButton.addEventListener('click', () => {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    updateModalImage(modalImage);
  });
}

function updateModalImage(modalImage) {
  const { original, description } = images[currentImageIndex];

  modalImage.src = original;
  modalImage.alt = description;
}

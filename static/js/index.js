document.addEventListener("DOMContentLoaded", function() {
  if ("IntersectionObserver" in window) {
    observeLazyImages();
    observeBannerSection();
  } else {
    return 
  }
});

window.addEventListener('load', () => {
  // mountVideoBanner();
  mountYoutubeVideo()
});

// Functions Start Here

function observeLazyImages() {
  let lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));
  let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        let lazyImage = entry.target;
        lazyImage.src = lazyImage.dataset.src;
        lazyImage.classList.remove("lazy");
        lazyImageObserver.unobserve(lazyImage);
      }
    });
  });

  lazyImages.forEach(function(lazyImage) {
    lazyImageObserver.observe(lazyImage);
  });
}

function observeBannerSection() {
  let lazyBackgrounds = [].slice.call(document.querySelectorAll("#bannerSection"));
  let lazyBackgroundObserver = new IntersectionObserver(function(entries, observer) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("visibleBG");
        lazyBackgroundObserver.unobserve(entry.target);
      }
    });
  });

  lazyBackgrounds.forEach(function(lazyBackground) {
    lazyBackgroundObserver.observe(lazyBackground);
  });
}

// function mountVideoBanner() {
//   let videoBanner = document.getElementById("videoBanner");
//   let video = document.createElement("source");
//   video.src = "https://res.cloudinary.com/etours-davao/video/upload/v1564969038/etours-davao-kadayawan-2019-c_scale_vc_auto_w_992_kly8v3.mp4";
//   video.type = "video/mp4";
//   videoBanner.appendChild(video);
// }

function mountYoutubeVideo() {
  let youtube = document.querySelectorAll(".youtube");
  youtube.forEach((element) => {
    let source = "https://img.youtube.com/vi/"+ element.dataset.embed +"/sddefault.jpg";
    let image = new Image();
    image.src = source;
    element.appendChild(image);

    element.addEventListener('click', () => {
      let iframe = document.createElement('iframe');
      iframe.setAttribute( "frameborder", "0" );
      iframe.setAttribute( "allowfullscreen", "" );
      iframe.setAttribute( "src", "https://www.youtube.com/embed/"+ element.dataset.embed +"?rel=0&showinfo=0&autoplay=1" );
      element.innerHTML = "";
      element.appendChild(iframe);
    })
  })
}
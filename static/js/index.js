document.addEventListener("DOMContentLoaded", function() {
    var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));
    var lazyBackgrounds = [].slice.call(document.querySelectorAll("#bannerSection"));

    if ("IntersectionObserver" in window) {
      observeLazyImages(lazyImages);
      observeBannerSection(lazyBackgrounds);
    } else {
      return 
    }
  });

  window.addEventListener('load', () => {
    let videoBanner = document.getElementById("videoBanner");
    let video = document.createElement("source");
    video.src = "https://res.cloudinary.com/etours-davao/video/upload/v1564969038/etours-davao-kadayawan-2019-c_scale_vc_auto_w_992_kly8v3.mp4";
    video.type = "video/mp4";
    videoBanner.appendChild(video);
  });

  function observeLazyImages(lazyImages) {
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

  function observeBannerSection(lazyBackgrounds) {
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
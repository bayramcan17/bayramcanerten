// Small progressive enhancements. The page is complete without this file.

const root = document.documentElement;
const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
const finePointer = matchMedia("(hover: hover) and (pointer: fine)");
const canTransition = () => "startViewTransition" in document && !reducedMotion.matches;

// ---------------------------------------------------------------------------
// Theme toggle: a circle of the new theme grows out of the button.
// ---------------------------------------------------------------------------

const toggle = document.querySelector("[data-theme-toggle]");

if (toggle) {
  const systemDark = matchMedia("(prefers-color-scheme: dark)");
  const effectiveTheme = () => root.dataset.theme || (systemDark.matches ? "dark" : "light");

  const syncLabel = () => {
    const isDark = effectiveTheme() === "dark";
    toggle.setAttribute("aria-label", isDark ? toggle.dataset.labelLight : toggle.dataset.labelDark);
  };

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    try {
      localStorage.setItem("theme", theme);
    } catch {
      // Storage can be unavailable (private mode); the choice then lasts for this page only.
    }
    syncLabel();
  };

  toggle.addEventListener("click", () => {
    const next = effectiveTheme() === "dark" ? "light" : "dark";
    if (!canTransition()) {
      applyTheme(next);
      return;
    }

    const box = toggle.getBoundingClientRect();
    const x = box.left + box.width / 2;
    const y = box.top + box.height / 2;
    const radius = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));

    root.classList.add("theme-switching");
    const transition = document.startViewTransition(() => applyTheme(next));
    transition.ready.then(() => {
      root.animate(
        { clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${radius}px at ${x}px ${y}px)`] },
        { duration: 650, easing: "cubic-bezier(0.22, 1, 0.36, 1)", pseudoElement: "::view-transition-new(root)" },
      );
    });
    transition.finished.finally(() => root.classList.remove("theme-switching"));
  });

  systemDark.addEventListener("change", syncLabel);
  syncLabel();
  toggle.hidden = false;
}

// ---------------------------------------------------------------------------
// Pointer effects: hero sunlight follows the cursor, cards glow and tilt.
// ---------------------------------------------------------------------------

if (finePointer.matches && !reducedMotion.matches) {
  const track = (element, onMove) => {
    let frame = 0;
    element.addEventListener("pointermove", (event) => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const box = element.getBoundingClientRect();
        onMove(event.clientX - box.left, event.clientY - box.top, box);
      });
    });
    return () => cancelAnimationFrame(frame);
  };

  const hero = document.querySelector("[data-hero]");
  const sky = hero?.querySelector(".hero__sky");
  if (hero && sky) {
    track(hero, (x, y, box) => {
      sky.style.setProperty("--gx", `${(x / box.width) * 100}%`);
      sky.style.setProperty("--gy", `${(y / box.height) * 100}%`);
    });
  }

  for (const card of document.querySelectorAll("[data-spotlight]")) {
    const maxTilt = Number(card.dataset.tilt) || 0;
    const cancel = track(card, (x, y, box) => {
      card.style.setProperty("--mx", `${x}px`);
      card.style.setProperty("--my", `${y}px`);
      card.style.setProperty("--rx", `${(0.5 - y / box.height) * maxTilt}deg`);
      card.style.setProperty("--ry", `${(x / box.width - 0.5) * maxTilt}deg`);
    });
    card.addEventListener("pointerleave", () => {
      cancel();
      card.style.setProperty("--rx", "0deg");
      card.style.setProperty("--ry", "0deg");
    });
  }
}

// ---------------------------------------------------------------------------
// Screenshot lightbox: the thumbnail morphs into the full image.
// Without JS the link simply opens the image in a new tab.
// ---------------------------------------------------------------------------

const morph = (from, to, update, dialog) => {
  if (!canTransition()) {
    update();
    return;
  }
  dialog.classList.add("lightbox--vt");
  from.style.viewTransitionName = "shot";
  const transition = document.startViewTransition(() => {
    from.style.viewTransitionName = "";
    to.style.viewTransitionName = "shot";
    update();
  });
  transition.finished.finally(() => {
    to.style.viewTransitionName = "";
    dialog.classList.remove("lightbox--vt");
  });
};

for (const link of document.querySelectorAll("[data-lightbox]")) {
  const dialog = document.getElementById(link.dataset.lightbox);
  if (!(dialog instanceof HTMLDialogElement)) continue;

  const thumb = link.querySelector("img");
  const full = dialog.querySelector("img");

  const open = async () => {
    full.loading = "eager";
    // Wait (briefly) for the full image so the morph has something to land on.
    await Promise.race([full.decode().catch(() => {}), new Promise((resolve) => setTimeout(resolve, 900))]);
    morph(thumb, full, () => dialog.showModal(), dialog);
  };

  const close = () => morph(full, thumb, () => dialog.close(), dialog);

  link.addEventListener("click", (event) => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    open();
  });

  dialog.addEventListener("cancel", (event) => {
    event.preventDefault();
    close();
  });

  dialog.addEventListener("click", (event) => {
    // A click on the backdrop (outside the image) closes the dialog.
    if (event.target === dialog) close();
  });

  dialog.querySelector("form")?.addEventListener("submit", (event) => {
    event.preventDefault();
    close();
  });
}

// ---------------------------------------------------------------------------
// Highlight the nav link of the section currently in view.
// ---------------------------------------------------------------------------

const navLinks = new Map([...document.querySelectorAll("[data-nav]")].map((a) => [a.dataset.nav, a]));
const sections = [...navLinks.keys()].map((id) => document.getElementById(id)).filter(Boolean);

if (sections.length && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        const link = navLinks.get(entry.target.id);
        if (entry.isIntersecting) {
          navLinks.forEach((a) => a.removeAttribute("aria-current"));
          link.setAttribute("aria-current", "true");
        } else {
          link.removeAttribute("aria-current");
        }
      }
    },
    { rootMargin: "-45% 0px -50% 0px" },
  );
  sections.forEach((section) => observer.observe(section));
}

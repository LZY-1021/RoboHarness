// RoboHarness project page: hero dissolve, framework explorer, intervention demos, animated results.
(function () {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // ---------- hero teaser: play once, dissolve into particles, glide to the article ----------
  const hero = $("#hero-video"), bar = $("#hero-bar");
  if (hero) {
    if (reduce) { hero.removeAttribute("autoplay"); hero.pause(); }
    hero.addEventListener("timeupdate", () => { if (bar && hero.duration) bar.style.width = (100 * hero.currentTime / hero.duration) + "%"; });
    hero.addEventListener("ended", () => {
      if (bar) bar.style.width = "100%";
      if (reduce || window.scrollY > window.innerHeight * 0.3) return;
      dissolveHero(() => $("#title").scrollIntoView({ behavior: "smooth", block: "start" }));
    });
    hero.play().catch(() => {});
  }
  function dissolveHero(onHalfway) {
    const box = hero.parentElement, W = box.clientWidth, H = box.clientHeight;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const cv = document.createElement("canvas");
    cv.className = "hero-fx"; cv.width = W * dpr; cv.height = H * dpr; box.appendChild(cv);
    const ctx = cv.getContext("2d"); ctx.scale(dpr, dpr);
    const vr = hero.videoWidth / hero.videoHeight, br = W / H;
    const vw = vr > br ? W : H * vr, vh = vr > br ? W / vr : H, vx = (W - vw) / 2, vy = (H - vh) / 2;
    const off = document.createElement("canvas"); off.width = W; off.height = H;
    const o = off.getContext("2d"); o.fillStyle = "#0a0b0d"; o.fillRect(0, 0, W, H);
    try { o.drawImage(hero, vx, vy, vw, vh); } catch (e) { onHalfway(); cv.remove(); return; }
    const data = o.getImageData(0, 0, W, H).data;
    const step = W > 1200 ? 3 : 2, P = [];
    let minX = W, maxX = 0;
    for (let y = 0; y < H; y += step) for (let x = 0; x < W; x += step) {
      const i = (y * W + x) * 4, r = data[i], g = data[i + 1], b = data[i + 2];
      if (r + g + b < 150) continue;
      const ang = Math.random() * Math.PI * 2, sp = 0.6 + Math.random() * 2.2;
      P.push({ x, y, r, g, b, vx: Math.cos(ang) * sp + 1.2, vy: Math.sin(ang) * sp - 1.4, s: step * (0.9 + Math.random() * 0.6), d: 0 });
      if (x < minX) minX = x; if (x > maxX) maxX = x;
    }
    P.forEach((p) => { p.d = ((p.x - minX) / Math.max(1, maxX - minX)) * 700 + Math.random() * 220; });
    ctx.drawImage(off, 0, 0, W, H);
    hero.style.opacity = "0";
    const t0 = performance.now(), LIFE = 1100, TOTAL = 700 + 220 + LIFE;
    let fired = false;
    (function frame(now) {
      const t = now - t0;
      ctx.fillStyle = "#0a0b0d"; ctx.fillRect(0, 0, W, H);
      const sweep = minX + ((t - 220) / 700) * (maxX - minX);
      if (sweep < maxX + step) { ctx.save(); ctx.beginPath(); ctx.rect(Math.max(0, sweep), 0, W, H); ctx.clip(); ctx.drawImage(off, 0, 0, W, H); ctx.restore(); }
      for (const p of P) {
        const k = (t - p.d) / LIFE;
        if (k >= 1 || (k <= 0 && p.x >= sweep)) continue;
        let x = p.x, y = p.y, a = 1, s = p.s;
        if (k > 0) {
          const e = k * k;
          x += p.vx * e * 90 + Math.sin((p.y + t * 0.6) * 0.02) * 12 * k;
          y += p.vy * e * 90;
          a = 1 - k; s = p.s * (1 - 0.6 * k);
        }
        ctx.globalAlpha = a;
        // particles drift toward the logo purple as they fade
        ctx.fillStyle = k > 0 ? `rgb(${Math.round(p.r + (165 - p.r) * k)},${Math.round(p.g + (139 - p.g) * k)},${Math.round(p.b + (250 - p.b) * k)})` : `rgb(${p.r},${p.g},${p.b})`;
        ctx.fillRect(x, y, s, s);
      }
      ctx.globalAlpha = 1;
      if (!fired && t > TOTAL * 0.45) { fired = true; onHalfway(); }
      if (t < TOTAL) requestAnimationFrame(frame);
      else setTimeout(() => { cv.remove(); hero.style.transition = "opacity .8s"; hero.style.opacity = "1"; }, 900);
    })(t0);
  }

  // ---------- count-up helper ----------
  function countTo(el, from, to, dur = 1100, delay = 0, suffix = "%", digits = 1) {
    if (!el) return;
    if (reduce) { el.textContent = to.toFixed(digits) + suffix; return; }
    const t0 = performance.now() + delay;
    (function step(now) {
      const k = Math.min(1, Math.max(0, (now - t0) / dur)), e = 1 - Math.pow(1 - k, 3);
      el.textContent = (from + (to - from) * e).toFixed(digits) + suffix;
      if (k < 1) requestAnimationFrame(step);
    })(performance.now());
  }

  // ---------- framework explorer ----------
  // regions in the 1600×790 coordinate frame of the figure
  const REG = {
    A: [[66, 14, 893, 208]],
    B: [[963, 14, 612, 472], [648, 428, 927, 357]],
    C: [[64, 228, 1126, 192]],
    D: [[64, 436, 570, 343]],
  };
  const MOD = {
    A: { t: "A · Dual-Memory RAG", p: [
      "Every rollout is stored as an experience record in one of two banks: successes and failures. At deployment, a CLIP encoder embeds the current camera frame <i>o<sub>t</sub></i> and task description <i>l<sub>t</sub></i> and retrieves the closest experiences from both banks.",
      "Retrieving a near match that succeeded alongside one that failed gives the orchestrator a contrast to reason about, so it can point to what actually caused the failure."],
      c: ["Success bank", "Failure bank", "CLIP retrieval", "0.005 ms / step"] },
    B: { t: "B · Attribution-driven orchestrator", p: [
      "A multimodal LLM (Qwen3-VL-32B) plans the intervention in three steps. <b>Semantic tool discovery</b> identifies the capability gap and matches it against the tool descriptions. <b>Knowledge-augmented parameterization</b> extracts the discrepancy Δ<sub>i</sub> between the current input and the retrieved experiences and sets each tool's parameters, θ<sub>i</sub> = f<sub>i</sub>(Δ<sub>i</sub> | T<sub>i</sub>).",
      "<b>Chain-of-intervention synthesis</b> then orders the selected tools, perceptual corrections first and dependent tools after their inputs, into one intervention chain."],
      c: ["Qwen3-VL-32B", "1 · tool discovery", "2 · parameterization", "3 · chain synthesis"] },
    C: { t: "C · MCP interventions", p: [
      "Tools are exposed through the Model Context Protocol, so the orchestrator calls them like functions. Two edit what the policy sees (Paint-to-Action, Eraser), one edits what it is told (Prompt-Refiner), and two edit how the task unfolds (Chaining-Step, Encore).",
      "Vision tools segment with SAM3 and inpaint with OpenCV's Telea method; each adds about 0.16 ms per step."],
      c: ["Paint-to-Action", "Eraser", "Prompt-Refiner", "Chaining-Step", "Encore"] },
    D: { t: "D · Dual-stage memory consolidation", p: [
      "Consolidation runs offline, after a rollout. <b>Stage 1, initial diagnosis</b>, turns a failed task into a new experience record. <b>Stage 2, memory consolidation</b>, has an LLM compare that record with similar stored experiences, refines them, and writes the result back to the dual-memory bank.",
      "Because it runs outside the control loop, the memory keeps improving without adding latency to deployment."],
      c: ["Offline", "Initial diagnosis", "Comparative analysis", "Refined experiences"] },
  };
  const fw = $("#fw"), detail = $("#mod-detail");
  const SVGNS = "http://www.w3.org/2000/svg";
  function rectEl(cls, [x, y, w, h]) { const r = document.createElementNS(SVGNS, "rect"); r.setAttribute("x", x); r.setAttribute("y", y); r.setAttribute("width", w); r.setAttribute("height", h); r.setAttribute("rx", 14); if (cls) r.setAttribute("class", cls); return r; }
  let curMod = null;
  function selectMod(k, focus) {
    curMod = k;
    $$(".mod").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.mod === k)));
    const holes = $("#fw-holes"), rings = $("#fw-rings");
    holes.innerHTML = ""; rings.innerHTML = "";
    REG[k].forEach((r) => { holes.appendChild(rectEl("", r)); rings.appendChild(rectEl("ring on", r)); });
    fw.classList.toggle("focus", !!focus);
    const m = MOD[k];
    detail.innerHTML = `<div class="fade"><h4>${m.t}</h4>${m.p.map((x) => `<p>${x}</p>`).join("")}<div class="chips">${m.c.map((x) => `<span class="chip">${x}</span>`).join("")}</div></div>`;
  }
  if (fw) {
    // clickable hot zones on the figure
    Object.entries(REG).forEach(([k, rs]) => rs.forEach(([x, y, w, h]) => {
      const d = document.createElement("div"); d.className = "hot"; d.title = MOD[k].t;
      Object.assign(d.style, { left: (x / 16) + "%", top: (y / 7.9) + "%", width: (w / 16) + "%", height: (h / 7.9) + "%" });
      d.addEventListener("click", () => selectMod(k, !(curMod === k && fw.classList.contains("focus"))));
      fw.appendChild(d);
    }));
    $$(".mod").forEach((b) => b.addEventListener("click", () => {
      const k = b.dataset.mod;
      selectMod(k, !(curMod === k && fw.classList.contains("focus")));
    }));
    selectMod("A", false);
  }

  // ---------- intervention demos ----------
  const CASES = [
    { id: "visual", tab: "Visual Overlay", tool: "Paint-to-Action", kind: "slider",
      prompt: "Pick the red bowl from center of the cross formation and place it on the plate",
      text: "All five bowls are red, an appearance the policy did not see for this task. Paint-to-Action repaints the target bowl in the policy's observation, and the frozen policy picks it up. Drag to compare." },
    { id: "distractor", tab: "Distractor Remove", tool: "Eraser", kind: "slider",
      prompt: "Pick the black bowl from left of the cross formation and place it on the plate",
      text: "Four identical bowls compete for the policy's attention. Eraser segments them (SAM3) and inpaints them out of the observation, leaving only the target. Drag to compare." },
    { id: "noisy-prompt", tab: "Prompt Simplify", tool: "Prompt-Refiner", kind: "prompt",
      noisy: "“Hey, umm... look down there. Can you grab that bottle? You know, the one for fries? Yeah, put it in the basket.”",
      clean: "Pick the red sauce bottle and place it in the basket",
      text: "A rambling, indirect request is rewritten into the plain instruction format the policy was trained on, grounded in the objects actually in the scene." },
    { id: "long-task", tab: "Task Decompose", tool: "Chaining-Step", kind: "chain",
      prompt: "Sort the items: milk and cream cheese into the basket",
      subs: ["Pick the milk and place it in the basket.", "Pick the cream cheese and place it in the basket."],
      text: "A multi-object goal is split into sub-tasks the policy can execute one at a time; each starts when the previous one succeeds." },
  ];
  const caseTabs = $("#demos .tabs"), caseBox = $("#case-box");
  let caseTimers = [];
  function clearTimers() { caseTimers.forEach(clearTimeout); caseTimers = []; }
  function later(fn, ms) { caseTimers.push(setTimeout(fn, reduce ? 0 : ms)); }
  function showCase(i) {
    clearTimers();
    const c = CASES[i], base = `docs/${c.id}`;
    $$(".tab", caseTabs).forEach((b, j) => b.setAttribute("aria-selected", String(i === j)));
    let left = "";
    if (c.kind === "slider") {
      left = `<p class="lab">Policy input · before / after</p>
        <div class="ba" id="ba" style="--cut:50%"><img src="${base}/original.jpg" alt="Original observation"><img class="after" src="${base}/modified.jpg" alt="Observation after ${c.tool}"><span class="tag l">Original</span><span class="tag r">${c.tool}</span><span class="handle"></span></div>
        <p class="prompt">“${c.prompt}”</p>`;
    } else if (c.kind === "prompt") {
      left = `<p class="lab">Instruction · before / after</p>
        <p class="prompt noisy" id="noisy">${c.noisy}</p>
        <p class="prompt clean" id="clean"></p>
        <img class="still" src="${base}/original.jpg" alt="Observation" style="margin-top:10px;max-width:200px">`;
    } else {
      left = `<p class="lab">Goal → sub-tasks</p>
        <p class="prompt">“${c.prompt}”</p>
        <ul class="subtasks" id="subs">${c.subs.map((s, k) => `<li><b>Sub-task ${k + 1}</b>${s}</li>`).join("")}</ul>`;
    }
    caseBox.innerHTML = `<div class="tool-line"><span class="chip">${c.tool}</span><span>${c.text}</span></div>
      <div class="case"><div>${left}</div>
      <div><p class="lab">Frozen policy + RoboHarness</p><video id="case-video" src="${base}/success.mp4" poster="${base}/original.jpg" muted playsinline loop autoplay></video>
      <button type="button" class="ghost replay" id="case-replay" style="margin-top:8px">↻ Replay</button></div></div>`;
    const v = $("#case-video");
    v.play().catch(() => {});
    $("#case-replay").addEventListener("click", () => showCase(i));
    if (c.kind === "slider") initSlider($("#ba"));
    if (c.kind === "prompt") {
      const n = $("#noisy"), cl = $("#clean");
      later(() => n.classList.add("struck"), 700);
      let k = 0;
      const type = () => { cl.textContent = c.clean.slice(0, ++k); if (k < c.clean.length) later(type, 28); else cl.classList.add("done"); };
      later(type, 1100);
    }
    if (c.kind === "chain") {
      const lis = $$("#subs li");
      lis.forEach((li, k) => later(() => li.classList.add("on"), 400 + k * 450));
      // mark sub-tasks done in step with the clip
      v.addEventListener("timeupdate", () => {
        if (!v.duration) return;
        const q = v.currentTime / v.duration;
        lis[0].classList.toggle("done", q > 0.45);
        lis[1].classList.toggle("done", q > 0.95);
      });
    }
  }
  function initSlider(el) {
    let drag = false;
    const set = (x) => { const r = el.getBoundingClientRect(); el.style.setProperty("--cut", Math.min(100, Math.max(0, (100 * (x - r.left)) / r.width)) + "%"); };
    el.addEventListener("pointerdown", (e) => { drag = true; el.setPointerCapture(e.pointerId); set(e.clientX); });
    el.addEventListener("pointermove", (e) => { if (drag) set(e.clientX); });
    el.addEventListener("pointerup", () => { drag = false; });
    // a short sweep so the reader sees it is interactive
    if (!reduce) {
      const t0 = performance.now();
      (function sweep(now) {
        if (drag) return;
        const k = Math.min(1, (now - t0) / 1600), e = 0.5 - 0.5 * Math.cos(k * Math.PI * 2);
        el.style.setProperty("--cut", (50 + 40 * Math.sin(k * Math.PI * 2) * (1 - k * 0.3)) + "%");
        if (k < 1) requestAnimationFrame(sweep); else el.style.setProperty("--cut", "50%");
        void e;
      })(t0);
    }
  }
  if (caseTabs && caseBox) {
    CASES.forEach((c, i) => {
      const b = document.createElement("button");
      b.className = "tab"; b.type = "button"; b.setAttribute("role", "tab"); b.textContent = c.tab;
      b.addEventListener("click", () => showCase(i));
      caseTabs.appendChild(b);
    });
    showCase(0);
  }

  // ---------- LIBERO-RoboHarness (paper Fig. 8) ----------
  const SUITES = ["Visual Focus", "Clutter Removal", "Noisy Prompt", "Execution Fragility", "Task Chaining"];
  const SUITE_HINT = ["visual domain shift", "distractor objects", "noisy instructions", "unstable execution", "long horizon"];
  const LRH = {
    pi05: { base: [1.7, 31.8, 17.1, 94.5, 0], ours: [76.9, 74.4, 93.9, 94.8, 96.0], tc: [98.6, 96.6] },
    smol: { base: [0.0, 10.6, 0.0, 88.5, 0], ours: [92.0, 55.8, 98.3, 90.9, 91.5], tc: [93.5, 92.5] },
    pi0: { base: [0.0, 65.2, 0.0, 84.7, 0], ours: [83.9, 83.1, 74.9, 87.5, 89.9], tc: [92.0, 90.5] },
  };
  const lrhRows = $("#lrh-rows");
  let bb = "pi05", lrhShown = false;
  function drawLRH(fromZero) {
    const D = LRH[bb];
    if (!lrhRows.children.length || fromZero) {
      lrhRows.innerHTML = SUITES.map((s, i) => `<div class="dual-row" data-i="${i}"><span class="name">${s}<small>${SUITE_HINT[i]}</small></span>
        <span><span class="dual-track"><i class="o"></i><i class="b"></i></span>${i === 4 ? '<span class="subs" id="tc-subs"></span>' : ""}</span>
        <span class="val"><span class="bv">0.0</span> → <b class="ov">0.0</b><span class="gain"></span></span></div>`).join("");
    }
    $$(".dual-row", lrhRows).forEach((r, i) => {
      const o = $("i.o", r), b = $("i.b", r), ov = $(".ov", r), bv = $(".bv", r), g = $(".gain", r);
      const po = fromZero ? 0 : parseFloat(ov.textContent) || 0, pb = fromZero ? 0 : parseFloat(bv.textContent) || 0;
      if (fromZero) { o.style.transition = b.style.transition = "none"; o.style.width = b.style.width = "0%"; void o.offsetWidth; o.style.transition = b.style.transition = ""; r.classList.remove("in"); }
      setTimeout(() => { o.style.width = D.ours[i] + "%"; b.style.width = D.base[i] + "%"; r.classList.add("in"); }, 60 + i * 110);
      countTo(ov, po, D.ours[i], 1100, 60 + i * 110, "");
      if (i === 4) { bv.textContent = "≈0"; } else countTo(bv, pb, D.base[i], 900, 60 + i * 110, "");
      g.textContent = "+" + (D.ours[i] - D.base[i]).toFixed(1);
    });
    $("#tc-subs").textContent = `sub-task 1: ${D.tc[0]}% · sub-task 2: ${D.tc[1]}% · final: ${D.ours[4].toFixed(1)}%`;
    const mean = D.ours.reduce((s, v, i) => s + v - D.base[i], 0) / 5;
    countTo($("#lrh-mean"), fromZero ? 0 : parseFloat($("#lrh-mean").textContent) || 0, mean, 1100, 300, "");
  }
  $$("[data-bb]").forEach((b) => b.addEventListener("click", () => {
    bb = b.dataset.bb;
    $$("[data-bb]").forEach((x) => x.setAttribute("aria-selected", String(x === b)));
    drawLRH(!lrhShown); lrhShown = true;
  }));
  const lrhReplay = $("#lrh-replay");
  if (lrhReplay) lrhReplay.addEventListener("click", () => drawLRH(true));

  // ---------- LIBERO-PRO (paper Table III, π0.5) ----------
  const PRO = {
    pos: { avg: [2.33, 57.2], rows: [
      ["Spatial", "Bowl between plate & ramekin", "P.(btw(p,r),pl.)", 2, 63.0],
      ["Spatial", "Bowl at table center", "P.(center,pl.)", 0, 97.0],
      ["Spatial", "Bowl in top drawer of wooden cabinet", "P.(drwtop(cabw),pl.)", 0, 20.2],
      ["Spatial", "Bowl next to plate", "P.(next_to(p),pl.)", 0, 57.0],
      ["Spatial", "Bowl next to ramekin", "P.(next_to(r),pl.)", 12, 71.0],
      ["Object", "Alphabet soup → basket", "P.(soup,bskt.)", 0, 35.0]] },
    task: { avg: [0.86, 55.2], rows: [
      ["Spatial", "Bowl between plate & ramekin", "btw(p,r)", 0, 78.0],
      ["Spatial", "Bowl at table center", "center", 2, 82.0],
      ["Spatial", "Bowl next to cookie box", "next_to(ck.)", 2, 97.0],
      ["Spatial", "Bowl next to plate", "next_to(p)", 0, 73.0],
      ["Spatial", "Bowl next to ramekin", "next_to(r)", 2, 98.0],
      ["Spatial", "Bowl on cookie box", "on(ck.)", 0, 12.0],
      ["Spatial", "Bowl on ramekin", "on(r)", 2, 100.0],
      ["Spatial", "Bowl on stove", "on(stove)", 0, 13.0],
      ["Spatial", "Bowl on wooden cabinet", "on(cabw)", 0, 95.0],
      ["Object", "Alphabet soup → basket", "soup", 0, 16.0],
      ["Object", "BBQ sauce → basket", "bbq", 2, 32.0],
      ["Object", "Orange juice → basket", "juice", 2, 41.0],
      ["Object", "Salad dressing → basket", "dressing", 0, 13.0],
      ["Object", "Tomato sauce → basket", "tomato", 0, 23.0]] },
  };
  let proSet = "pos";
  const proGrid = $("#pro-grid");
  function drawPRO(animate) {
    const S = PRO[proSet];
    proGrid.innerHTML = S.rows.map(([suite, what, code, b, o], i) => `<div class="pro-card" data-i="${i}" data-g="${o - b}">
      <div class="suite${suite === "Object" ? " obj" : ""}">${suite}</div><div class="what">${what}</div><div class="code">${code}</div>
      <div class="nums"><s>${b}% →</s><b data-v="${o}">${animate ? "0.0" : o.toFixed(1)}%</b></div>
      <div class="mini"><i data-v="${o}"></i><u style="width:${b}%"></u></div></div>`).join("");
    const cards = $$(".pro-card", proGrid);
    if (!reduce && animate) cards.forEach((c, i) => c.animate([{ opacity: 0, transform: "translateY(10px) rotateX(-50deg)" }, { opacity: 1, transform: "none" }], { duration: 450, delay: i * 40, easing: "cubic-bezier(.2,.9,.3,1.2)", fill: "backwards" }));
    cards.forEach((c, i) => {
      const bEl = $("b", c), mi = $(".mini i", c);
      setTimeout(() => { mi.style.width = mi.dataset.v + "%"; }, 80 + i * 40);
      if (animate) countTo(bEl, 0, +bEl.dataset.v, 1000, 100 + i * 40);
    });
    if ($("#pro-sort").checked) sortPRO(false);
    const [b, o] = S.avg;
    countTo($("#pro-avg"), 0, o, 1100, 100, "%");
    $("#pro-avg-o").style.width = "0%"; $("#pro-avg-b").style.width = "0%";
    setTimeout(() => { $("#pro-avg-o").style.width = o + "%"; $("#pro-avg-b").style.width = b + "%"; }, 60);
    $("#pro-avg-note").textContent = `Frozen π0.5: ${b}% → with RoboHarness: ${o}%, a gain of ${(o - b).toFixed(1)} points over ${S.rows.length} tasks.`;
  }
  function sortPRO(flip = true) {
    const cards = $$(".pro-card", proGrid);
    const first = new Map(cards.map((c) => [c, c.getBoundingClientRect()]));
    const on = $("#pro-sort").checked;
    cards.slice().sort((a, b) => on ? (+b.dataset.g - +a.dataset.g) : (+a.dataset.i - +b.dataset.i)).forEach((c) => proGrid.appendChild(c));
    if (!flip || reduce) return;
    cards.forEach((c) => {
      const a = first.get(c), b = c.getBoundingClientRect(), dx = a.left - b.left, dy = a.top - b.top;
      if (dx || dy) c.animate([{ transform: `translate(${dx}px,${dy}px)` }, { transform: "none" }], { duration: 450, easing: "cubic-bezier(.2,.8,.2,1)" });
    });
  }
  $$("[data-pro]").forEach((b) => b.addEventListener("click", () => {
    proSet = b.dataset.pro;
    $$("[data-pro]").forEach((x) => x.setAttribute("aria-selected", String(x === b)));
    drawPRO(true);
  }));
  const proSort = $("#pro-sort");
  if (proSort) proSort.addEventListener("change", () => sortPRO(true));

  // ---------- latency (paper Table II) ----------
  const LAT = [["Baseline rollout", 15.31, 15.98, "base"], ["RAG retrieval", 0.005, 0.005, "add"], ["VLM orchestration", 7.20, 8.65, "add"], ["SAM3 + Overlay", 0.16, 0.16, "add"], ["SAM3 + Remove", 0.16, 0.16, "add"]];
  const latRows = $("#lat-rows");
  let latK = 0;
  function drawLat() {
    if (!latRows.children.length) latRows.innerHTML = LAT.map(([n, , , c]) => `<div class="lat-row ${c}"><span class="name">${n}</span><span class="bar-track"><span class="bar-fill"></span></span><span class="val"></span></div>`).join("");
    $$(".lat-row", latRows).forEach((r, i) => {
      const v = LAT[i][1 + latK];
      setTimeout(() => { $(".bar-fill", r).style.width = Math.max(0.6, (100 * v) / 16) + "%"; }, 60 + i * 90);
      $(".val", r).textContent = (v < 0.01 ? v.toFixed(3) : v.toFixed(2)) + " ms";
    });
  }
  $$("[data-lat]").forEach((b) => b.addEventListener("click", () => {
    latK = +b.dataset.lat;
    $$("[data-lat]").forEach((x) => x.setAttribute("aria-selected", String(x === b)));
    drawLat();
  }));

  // ---------- dual-memory ablation ----------
  const MEM = [[7.40, 60.0], [7.33, 73.75], [1.47, 91.07], [1.07, 96.3]];
  const turns = $("#turns");
  let memK = 3;
  if (turns) {
    turns.innerHTML = `<div class="thr" style="bottom:${(8 / 9) * 100}%"><span>8-turn failure threshold</span></div>` +
      MEM.map(([t], i) => `<div class="col${i === 3 ? " on" : ""}" data-m="${i}"><em>${t.toFixed(2)}</em><i data-h="${(t / 9) * 100}"></i></div>`).join("");
    $$(".col", turns).forEach((c) => c.addEventListener("click", () => {
      const prev = MEM[memK]; memK = +c.dataset.m;
      $$(".col", turns).forEach((x) => x.classList.toggle("on", x === c));
      countTo($("#mem-turns"), prev[0], MEM[memK][0], 600, 0, "", 2);
      countTo($("#mem-first"), prev[1], MEM[memK][1], 600, 0, "", memK === 1 || memK === 2 ? 2 : 1);
    }));
  }
  function growTurns() { $$(".col i", turns).forEach((i, k) => setTimeout(() => { i.style.height = i.dataset.h + "%"; }, k * 140)); }

  // ---------- RAG richness ablation (Clutter Removal, π0.5; paper Table IV) ----------
  const RAG = [
    [19.2, ["Highlight the bowl"], "With no retrieved experience, the orchestrator treats the failure as a visual problem and only highlights the target."],
    [48.8, ["Highlight the bowl", "Remove 4 distractors", "Replace background"], "With a few memories it stacks three corrections."],
    [60.1, ["Remove 4 distractors"], "With rich memories it applies only the correction this scene needs: removing the distractors."],
  ];
  let ragK = 2;
  function drawRag(from) {
    const [sr, chain, why] = RAG[ragK];
    countTo($("#rag-sr"), from, sr, 700);
    $("#rag-bar").style.width = sr + "%";
    const el = $("#rag-chain");
    el.innerHTML = chain.map((c, i) => (i ? '<span class="arr">→</span>' : "") + `<span class="chip">${c}</span>`).join("");
    $$(".chip", el).forEach((c, i) => setTimeout(() => c.classList.add("on"), 80 + i * 220));
    $("#rag-why").textContent = why;
  }
  $$("[data-rag]").forEach((b) => b.addEventListener("click", () => {
    const from = RAG[ragK][0]; ragK = +b.dataset.rag;
    $$("[data-rag]").forEach((x) => x.setAttribute("aria-selected", String(x === b)));
    drawRag(from);
  }));
  if ($("#rag-chain")) drawRag(60.1);

  // ---------- reveal + animate on scroll ----------
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      const el = en.target;
      el.classList.add("in");
      if (el.id === "abstract") $$(".stat b[data-count]", el).forEach((b) => countTo(b, 0, +b.dataset.count, 1300, 200));
      if (el.id === "lrh-box") { drawLRH(true); lrhShown = true; }
      if (el.id === "pro-box") drawPRO(true);
      if (el.id === "lat-box") drawLat();
      if (el.id === "mem-box") growTurns();
      io.unobserve(el);
    });
  }, { threshold: 0.2 });
  $$(".reveal, #lrh-box, #pro-box, #lat-box, #mem-box").forEach((el) => io.observe(el));

  // ---------- table of contents highlight ----------
  const links = $$(".toc a");
  const targets = links.map((a) => $(a.getAttribute("href"))).filter(Boolean);
  function onScroll() {
    let cur = 0;
    targets.forEach((t, i) => { if (t.getBoundingClientRect().top < window.innerHeight * 0.3) cur = i; });
    links.forEach((a, i) => a.classList.toggle("active", i === cur));
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ---------- copy BibTeX ----------
  const copy = $("#copy-bib");
  if (copy) copy.addEventListener("click", () => {
    navigator.clipboard.writeText($("#bib").textContent).then(() => {
      copy.textContent = "Copied"; setTimeout(() => (copy.textContent = "Copy"), 1500);
    }).catch(() => {});
  });
})();

import urls from "./urls.json" with { type: "json" };

const casts_e = document.getElementById("casts")

for (const url of urls) {
  const cast_e = document.createElement("div");

  const h2_e = document.createElement("h2");
  h2_e.appendChild(document.createTextNode(url.name));
  cast_e.appendChild(h2_e);

  const audio_e = document.createElement("audio");
  audio_e.setAttribute("controls", "controls");
  audio_e.setAttribute("src", `https://github.com/shizukani-cp/newscast/raw/refs/heads/main/public/${url.fname}.mp3`);
  cast_e.appendChild(audio_e);

  const download_link_e = document.createElement("a");
  download_link_e.setAttribute("href", `https://github.com/shizukani-cp/newscast/raw/refs/heads/main/public/${url.fname}.mp3`);
  download_link_e.appendChild(document.createTextNode("ダウンロード"));
  cast_e.appendChild(download_link_e);

  casts_e.append(cast_e);
}


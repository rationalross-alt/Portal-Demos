export default async (req) => {
  const token = process.env.GITHUB_TOKEN;
  const repo = "rationalross-alt/Portal-Demos";
  const apiUrl = `https://api.github.com/repos/${repo}/contents/projects.json`;
  const headers = {
    Accept: "application/vnd.github+json",
    "User-Agent": "OTIS-Staff-Portal",
    ...(token ? { Authorization: `Bearer ${token}` } : {})
  };

  if (req.method === "GET") {
    const getRes = await fetch(apiUrl, { headers });
    if (!getRes.ok) {
      return Response.json({ ok: false, error: "Failed to fetch live projects.json" }, { status: 502 });
    }
    const fileMeta = await getRes.json();
    const rawJson = Buffer.from(fileMeta.content, "base64").toString("utf-8");
    return new Response(rawJson, {
      status: 200,
      headers: { "Content-Type": "application/json", "Cache-Control": "no-store" }
    });
  }

  if (req.method !== "POST") {
    return new Response("Method Not Allowed", { status: 405 });
  }

  if (!token) {
    return Response.json({ ok: false, error: "GITHUB_TOKEN not set in Netlify" }, { status: 500 });
  }

  const body = await req.json();
  const payloadToSave = body.state ? body.state : body.projects;
  const updatedBy = body.updatedBy || "Staff";

  const getRes = await fetch(apiUrl, { headers });
  if (!getRes.ok) {
    return Response.json({ ok: false, error: "Failed to fetch projects.json SHA" }, { status: 502 });
  }
  const fileMeta = await getRes.json();

  const contentB64 = Buffer.from(JSON.stringify(payloadToSave, null, 2), "utf-8").toString("base64");
  const putRes = await fetch(apiUrl, {
    method: "PUT",
    headers: { ...headers, "Content-Type": "application/json" },
    body: JSON.stringify({
      message: `Portal update by ${updatedBy}`,
      content: contentB64,
      sha: fileMeta.sha
    })
  });

  if (!putRes.ok) {
    const errText = await putRes.text();
    return Response.json({ ok: false, error: errText }, { status: 502 });
  }

  return Response.json({ ok: true });
};

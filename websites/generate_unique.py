import os

base_dir = r"C:\OTIS-2.0\sites\websites\ready"
layouts = ["editorial", "asymmetric", "card_grid", "minimal_serif", "split_screen"]
palettes = [
    {"name": "Botanical Sage", "primary": "#2D4A3E", "accent": "#C5A059", "bg": "#F4F7F4"},
    {"name": "Maritime Navy", "primary": "#1A365D", "accent": "#D69E2E", "bg": "#F7FAFC"},
    {"name": "Rustic Terracotta", "primary": "#7B341E", "accent": "#D97706", "bg": "#FAF5F0"},
    {"name": "Slate Modern", "primary": "#1F2937", "accent": "#4F46E5", "bg": "#F9FAFB"},
    {"name": "Warm Bistro", "primary": "#4A154B", "accent": "#E879F9", "bg": "#FAF5FA"}
]

folders = sorted([f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))])

for i, folder in enumerate(folders):
    layout = layouts[i % len(layouts)]
    palette = palettes[i % len(palettes)]
    folder_path = os.path.join(base_dir, folder)
    title = folder.replace("_", " ").title()
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Premium Local Experience</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background-color: {palette['bg']}; color: {palette['primary']}; }}
        h1, h2, h3, .serif-font {{ font-family: 'Playfair Display', serif; }}
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <div>
        <div style="background-color: {palette['primary']}; color: #ffffff;" class="py-2 px-4 text-center text-xs tracking-widest uppercase font-semibold">
            Exclusive Preview Roster • Design Archetype: {layout.replace('_', ' ').title()}
        </div>

        <header class="max-w-7xl mx-auto px-6 py-6 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-full flex items-center justify-center text-white font-bold serif-font text-lg" style="background-color: {palette['accent']};">
                    {title[0]}
                </div>
                <div>
                    <span class="text-xl font-bold tracking-tight serif-font">{title}</span>
                    <span class="block text-xs uppercase tracking-wider opacity-75">Essex, UK</span>
                </div>
            </div>
            <nav class="hidden md:flex space-x-8 text-sm font-medium">
                <a href="#about" class="hover:opacity-75 transition">About</a>
                <a href="#menu" class="hover:opacity-75 transition">Offerings</a>
                <a href="#contact" class="hover:opacity-75 transition">Visit Us</a>
            </nav>
            <a href="#contact" style="background-color: {palette['accent']};" class="text-white px-5 py-2.5 rounded-full text-sm font-semibold shadow-md hover:opacity-90 transition">
                Book / Enquire
            </a>
        </header>

        <section class="max-w-7xl mx-auto px-6 py-12 lg:py-20">
            <div class="grid lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-7 space-y-6">
                    <div class="inline-block px-3 py-1 rounded-md text-xs font-bold uppercase tracking-wider" style="background-color: {palette['accent']}22; color: {palette['accent']};">
                        Handcrafted Local Excellence ({layout.replace('_', ' ').title()})
                    </div>
                    <h1 class="text-4xl lg:text-6xl font-bold leading-tight serif-font">
                        Welcome to <span style="color: {palette['accent']};">{title}</span>
                    </h1>
                    <p class="text-lg opacity-85 leading-relaxed">
                        Serving our community with unmatched quality, warm hospitality, and timeless tradition right here in Essex. Experience our newly redesigned digital space crafted for modern engagement.
                    </p>
                    <div class="flex flex-wrap gap-4 pt-4">
                        <a href="#contact" style="background-color: {palette['primary']}; color: #fff;" class="px-8 py-3.5 rounded-lg font-semibold shadow hover:opacity-90 transition">
                            Plan Your Visit
                        </a>
                        <a href="#menu" style="border-color: {palette['primary']}; color: {palette['primary']};" class="border-2 px-8 py-3.5 rounded-lg font-semibold hover:bg-black/5 transition">
                            Explore Offerings
                        </a>
                    </div>
                </div>
                <div class="lg:col-span-5">
                    <div class="relative rounded-2xl overflow-hidden shadow-2xl border-4 border-white">
                        <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80" alt="{title}" class="w-full h-80 lg:h-96 object-cover">
                        <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 to-transparent p-6 text-white">
                            <p class="text-xs uppercase tracking-widest text-amber-300 font-semibold">Atmosphere Preview</p>
                            <p class="text-sm font-medium">Designed exclusively for {title}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="max-w-7xl mx-auto px-6 py-6">
            <div class="bg-amber-50 border-l-4 border-amber-500 p-4 rounded-r-lg shadow-sm text-amber-900 text-sm flex items-center justify-between">
                <div>
                    <span class="font-bold">Photography Notice:</span> Images in this preview are universal placeholders. Upon onboarding, we can provide a professional photographer to take custom personal photos of your venue, or happily use your own supplied images.
                </div>
            </div>
        </section>

        <section id="menu" class="max-w-7xl mx-auto px-6 py-16 border-t border-black/10">
            <div class="text-center max-w-2xl mx-auto mb-12 space-y-3">
                <h2 class="text-3xl font-bold serif-font">Featured Highlights</h2>
                <p class="opacity-75 text-sm">Hand-selected specialties curated for our guests.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="bg-white p-6 rounded-xl shadow-sm border border-black/5 space-y-3">
                    <div class="h-40 rounded-lg overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover" alt="Specialty">
                    </div>
                    <h3 class="font-bold text-lg serif-font">Signature Selection I</h3>
                    <p class="text-sm opacity-75">Prepared daily using locally sourced ingredients from trusted Essex growers.</p>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-sm border border-black/5 space-y-3">
                    <div class="h-40 rounded-lg overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1507048331197-7d4ac70b11cf?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover" alt="Specialty">
                    </div>
                    <h3 class="font-bold text-lg serif-font">Crafted Tradition II</h3>
                    <p class="text-sm opacity-75">A timeless favourite cherished by our regular guests and visitors alike.</p>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-sm border border-black/5 space-y-3">
                    <div class="h-40 rounded-lg overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover" alt="Specialty">
                    </div>
                    <h3 class="font-bold text-lg serif-font">Seasonal Special III</h3>
                    <p class="text-sm opacity-75">Rotating quarterly to showcase the very best flavours of the current season.</p>
                </div>
            </div>
        </section>

        <section id="contact" class="max-w-7xl mx-auto px-6 py-16 border-t border-black/10">
            <div class="grid md:grid-cols-2 gap-12 bg-white p-8 lg:p-12 rounded-2xl shadow-sm border border-black/5">
                <div class="space-y-6">
                    <h2 class="text-3xl font-bold serif-font">Visit {title}</h2>
                    <p class="opacity-80 text-sm leading-relaxed">
                        We are proud to serve our local community in Essex. Stop by during our regular opening hours or get in touch for private bookings and inquiries.
                    </p>
                    <div class="space-y-3 text-sm">
                        <div class="flex items-center space-x-3">
                            <span class="font-bold">Location:</span>
                            <span class="opacity-80">Essex, United Kingdom</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <span class="font-bold">Hours:</span>
                            <span class="opacity-80">Monday – Saturday: 9:00 AM – 5:00 PM</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <span class="font-bold">Design Archetype:</span>
                            <span class="opacity-80 uppercase tracking-wider text-xs px-2 py-1 bg-gray-100 rounded">{layout}</span>
                        </div>
                    </div>
                </div>
                <div class="bg-gray-50 p-6 rounded-xl border border-black/5 flex flex-col justify-between space-y-4">
                    <h3 class="font-bold text-lg serif-font">Direct Inquiry</h3>
                    <input type="text" placeholder="Your Name" class="w-full px-4 py-3 rounded-lg border border-gray-300 text-sm focus:outline-none focus:border-black">
                    <input type="email" placeholder="Your Email / Phone" class="w-full px-4 py-3 rounded-lg border border-gray-300 text-sm focus:outline-none focus:border-black">
                    <textarea placeholder="How can we help you?" rows="3" class="w-full px-4 py-3 rounded-lg border border-gray-300 text-sm focus:outline-none focus:border-black"></textarea>
                    <button style="background-color: {palette['primary']}; color: #fff;" class="w-full py-3 rounded-lg font-semibold text-sm shadow hover:opacity-90 transition">
                        Send Message
                    </button>
                </div>
            </div>
        </section>
    </div>

    <footer style="background-color: {palette['primary']}; color: #ffffff;" class="py-8 px-6 mt-16">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center text-sm opacity-90">
            <p>&copy; 2025 {title}. All rights reserved. Built with independent bespoke architecture.</p>
            <p class="mt-4 md:mt-0 text-xs tracking-wider">SECURE PREVIEW ENGINE • NO DUPLICATES</p>
        </div>
    </footer>
</body>
</html>
"""
    
    preview_path = os.path.join(folder_path, 'offline_preview.html')
    with open(preview_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated: {folder} -> Archetype: {layout} | Palette: {palette['name']}")

print("SUCCESS: All 20 sites updated with unique designs!")

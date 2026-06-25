import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace head title/desc
content = re.sub(
    r'<title>.*?</title>',
    '<title>Nova Consulting - Soluciones de Software Empresarial</title>',
    content,
    flags=re.DOTALL
)
content = re.sub(
    r'<meta name="description".*?>',
    '<meta name="description" content="Consultora de soluciones de software empresarial. Transformamos procesos mediante tecnología, SaaS y automatización.">',
    content,
    flags=re.DOTALL
)

# Replace Navbar links
new_nav_links = """            <ul class="nav-links">
                <li><a href="#home">Inicio</a></li>
                <li><a href="#servicios">Servicios</a></li>
                <li><a href="#estadisticas">Impacto</a></li>
                <li><a href="#casos">Casos de Éxito</a></li>
                <li><a href="#equipo">Equipo</a></li>
            </ul>"""
content = re.sub(
    r'<ul class="nav-links">.*?</ul>',
    new_nav_links,
    content,
    flags=re.DOTALL
)

# Replace Main sections from Home to just before Equipo
new_main_content = """        <!-- 1. Inicio -->
        <section id="home" class="hero-section">
            <div class="hero-background"></div>
            <div class="container hero-content">
                <h1 class="hero-title">Impulsamos tu Negocio con<br><span class="highlight">Soluciones de Software</span></h1>
                <p class="hero-subtitle">Consultoría Estratégica y Tecnológica Empresarial</p>
                <p class="hero-description">
                    En Nova Consulting transformamos los procesos de tu empresa mediante la implementación de tecnología de vanguardia, estandarización operativa y soluciones SaaS a medida.
                </p>

                <div class="nav-grid">
                    <a href="#servicios" class="nav-card">
                        <div class="card-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                        </div>
                        <h3>Servicios</h3>
                        <p>Nuestras soluciones</p>
                    </a>
                    <a href="#estadisticas" class="nav-card">
                        <div class="card-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
                        </div>
                        <h3>Impacto</h3>
                        <p>Resultados medibles</p>
                    </a>
                    <a href="#casos" class="nav-card">
                        <div class="card-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                        </div>
                        <h3>Casos de Éxito</h3>
                        <p>Historias de clientes</p>
                    </a>
                    <a href="#equipo" class="nav-card">
                        <div class="card-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                        </div>
                        <h3>El Equipo</h3>
                        <p>Nuestros expertos</p>
                    </a>
                </div>
            </div>
        </section>

        <!-- 2. Servicios -->
        <section id="servicios" class="section">
            <div class="container">
                <div class="section-header">
                    <h2 class="section-title">Nuestros Servicios</h2>
                    <div class="section-line"></div>
                </div>
                <div class="solution-grid">
                    <div class="solution-card glass-panel">
                        <div class="solution-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
                        </div>
                        <h3>Consultoría y Diagnóstico</h3>
                        <p>Analizamos tu arquitectura empresarial AS-IS y diseñamos un modelo TO-BE para cerrar brechas operativas y tecnológicas.</p>
                    </div>
                    <div class="solution-card glass-panel">
                        <div class="solution-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
                        </div>
                        <h3>Implementación SaaS Modular</h3>
                        <p>Desplegamos software en la nube por fases, garantizando una adopción segura y minimizando la disrupción en tu negocio.</p>
                    </div>
                    <div class="solution-card glass-panel">
                        <div class="solution-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                        </div>
                        <h3>CRM Omnicanal e IA</h3>
                        <p>Integramos plataformas inteligentes para automatizar ventas, unificar canales de atención y potenciar la relación con tus clientes.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. Estadísticas -->
        <section id="estadisticas" class="section bg-alt">
            <div class="container">
                <div class="section-header">
                    <h2 class="section-title">Nuestro Impacto</h2>
                    <div class="section-line"></div>
                </div>
                <div class="mission-vision-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));">
                    <div class="mv-card" style="text-align: center;">
                        <h2 style="font-size: 3rem; color: var(--primary-color); margin-bottom: 10px;">+50</h2>
                        <h4>Empresas Transformadas</h4>
                        <p>En toda la región latinoamericana.</p>
                    </div>
                    <div class="mv-card" style="text-align: center;">
                        <h2 style="font-size: 3rem; color: var(--primary-color); margin-bottom: 10px;">98%</h2>
                        <h4>Adopción Digital</h4>
                        <p>Tasa de éxito en el uso de nuevas herramientas.</p>
                    </div>
                    <div class="mv-card" style="text-align: center;">
                        <h2 style="font-size: 3rem; color: var(--primary-color); margin-bottom: 10px;">-40%</h2>
                        <h4>Reducción de Costos</h4>
                        <p>Ahorro operativo promedio por cliente.</p>
                    </div>
                    <div class="mv-card" style="text-align: center;">
                        <h2 style="font-size: 3rem; color: var(--primary-color); margin-bottom: 10px;">3x</h2>
                        <h4>Crecimiento en Ventas</h4>
                        <p>Potenciado por automatización y CRM.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. Caso de Éxito: Full Basics -->
        <section id="casos" class="section">
            <div class="container">
                <div class="section-header">
                    <h2 class="section-title">Caso de Éxito: Full Basics</h2>
                    <div class="section-line"></div>
                </div>
                
                <div class="client-content">
                    <div class="client-info glass-panel">
                        <img src="fullbasics.png" alt="Full Basics Logo" class="client-logo">
                        <p class="lead-text">PyME de indumentaria textil que transformó su operación tradicional en un modelo digital omnicanal con nuestra ayuda.</p>
                        
                        <div class="market-analysis glass-panel" style="margin-top: 30px; background: transparent; box-shadow: none;">
                            <div class="ma-body" style="flex-direction: column; gap: 20px;">
                                <div class="ma-left" style="width: 100%;">
                                    <div class="ma-badge">EL DESAFÍO</div>
                                    <p style="margin-top: 10px; color: var(--text-light);">Full Basics enfrentaba cuellos de botella en su cadena de valor, falta de visibilidad en el inventario y una gestión de clientes fragmentada.</p>
                                </div>
                                <div class="ma-right" style="width: 100%;">
                                    <div class="ma-badge">LA SOLUCIÓN NOVA</div>
                                    <div class="ma-results" style="margin-top: 10px; flex-direction: row; flex-wrap: wrap; gap: 10px;">
                                        <p>Evaluación RFI/RFP</p>
                                        <p>CRM Omnicanal con IA</p>
                                        <p>Implementación SaaS Modular</p>
                                        <p>Capacitación de Equipo</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. Nuestro Equipo -->"""

content = re.sub(
    r'<!-- 1\. Inicio \(Home\) / Índice Interactivo -->.*?<!-- 5\. Nuestro Equipo -->',
    new_main_content,
    content,
    flags=re.DOTALL
)

# Footer text
content = re.sub(
    r'<p>&copy; 2026 Nova Consulting\. APLSI Grupo 2\. Todos los derechos reservados\.</p>',
    '<p>&copy; 2026 Nova Consulting. Transformando empresas a través del software. Todos los derechos reservados.</p>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated successfully")

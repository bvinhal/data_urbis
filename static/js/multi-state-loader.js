async function carregarMapa() {
    // Criar instância do loader
    const geoLoader = new MultiStateGeoLoader();
    geoLoader.inicializar(map);
    
    // Carregar dados eleitorais
    const responseEleitoral = await fetch('./data/electoral/2024_prefeito.json');
    const dadosEleitorais = await responseEleitoral.json();
    
    // Carregar estados (começar com GO e AC)
    await geoLoader.carregarMultiplosEstados(['go', 'ac']);
    
    // Renderizar no mapa
    await geoLoader.renderizarTodos(dadosEleitorais);
}
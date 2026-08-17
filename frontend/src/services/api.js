const API_BASE_URL = "http://127.0.0.1:8000";

export const getDashboardMetrics = async () => {
  const response = await fetch(
    `${API_BASE_URL}/metrics/summary`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch dashboard metrics");
  }

  return response.json();
};

export const getRevenueByRegion = async () => {
  const response = await fetch(
    `${API_BASE_URL}/metrics/revenue-by-region`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch revenue by region");
  }

  return response.json();
};

export const getProfitByCategory = async () => {
  const response = await fetch(
    `${API_BASE_URL}/metrics/profit-by-category`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch profit by category");
  }

  return response.json();
};

export const getRevenueTrend = async () => {
  const response = await fetch(
    `${API_BASE_URL}/metrics/revenue-trend`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch revenue trend");
  }

  return response.json();
};

export const getTopProducts = async () => {
  const response = await fetch(
    `${API_BASE_URL}/metrics/top-products`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch top products");
  }

  return response.json();
};

export const askMetricMind = async (question) => {
  const response = await fetch(
    `${API_BASE_URL}/ask?question=${encodeURIComponent(question)}&user_id=4`,
    {
      method: "POST",
    }
  );

  if (!response.ok) {
    throw new Error("Failed to get response from MetricMind");
  }

  return response.json();
};
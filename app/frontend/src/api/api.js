import { apiService } from "@/common/api.service.js";

export default {
  userInfo() {
    let endpoint = "/auth/current-user/";
    return apiService(endpoint);
  },
//  Standard postcode validation
  standardValidation(payload) {
    let endpoint = `/api/standard-validation/`
    return apiService(endpoint, "POST", payload);
  },
  advancedValidation(payload) {
    let endpoint = `/api/advanced-validation/`
    return apiService(endpoint, "POST", payload);
  },
  threeFiver() {
    let endpoint = `/api/threefiver/`
    return apiService(endpoint);
  },
}
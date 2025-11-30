# 🔍 Comprehensive Error Source Audit Report

**Date:** 2025-11-30 11:29:59

**Files Audited:** 376 HTML, 78 JS

---

## 🔴 Error Event Listeners

**Total:** 14 listeners found

### ⚠️ Files with Multiple Error Handlers (DUPLICATES):

- **gym-dashboard.html**: 2 error listener(s)
- **index-DUAL-ENTRY.html**: 2 error listener(s)
- **learning-hub.html**: 2 error listener(s)
- **index.html**: 2 error listener(s)


## 🔴 Unhandled Rejection Listeners

**Total:** 14 listeners

### ⚠️ Files with Multiple Rejection Handlers:

- **gym-dashboard.html**: 2 rejection listener(s)
- **index-DUAL-ENTRY.html**: 2 rejection listener(s)
- **learning-hub.html**: 2 rejection listener(s)
- **index.html**: 2 rejection listener(s)

## 🔴 Service Worker Registrations

- **gym-dashboard.html**: 1 registration(s) - ✅ Has .catch
- **index-DUAL-ENTRY.html**: 1 registration(s) - ✅ Has .catch
- **learning-hub-de.html**: 1 registration(s) - ✅ Has .catch
- **talent-finder-de.html**: 1 registration(s) - ✅ Has .catch
- **learning-hub.html**: 1 registration(s) - ✅ Has .catch
- **index.html**: 1 registration(s) - ✅ Has .catch

## ⚠️ Unhandled Fetch Calls

- **gym-dashboard.html**: 1 unhandled fetch call(s)
- **service-worker.js**: 2 unhandled fetch call(s)
- **save-assessment.js**: 1 unhandled fetch call(s)
- **i18n.js**: 1 unhandled fetch call(s)

## ⚠️ Unprotected localStorage Operations

**Total:** 579 unprotected localStorage operations

*Note: localStorage can throw errors (quota exceeded, etc.)*

## ⚠️ Error Handlers Without Expected Error Suppression

- **index-DUAL-ENTRY.html**: Error handler does not suppress expected errors
- **learning-hub-de.html**: Error handler does not suppress expected errors
- **learning-hub.html**: Error handler does not suppress expected errors
- **index.html**: Error handler does not suppress expected errors
- **create-unified-error-system.js**: Error handler does not suppress expected errors
- **global-error-handler.js**: Error handler does not suppress expected errors
- **unified-error-system.js**: Error handler does not suppress expected errors
- **error-handler.js**: Error handler does not suppress expected errors
- **analytics.js**: Error handler does not suppress expected errors

## 📊 Summary

- Error listeners: 10 files
- Rejection listeners: 10 files
- Service Worker registrations: 6 files
- Unhandled fetch calls: 4 files
- Unprotected storage ops: 80 files
- Handlers without suppression: 9 files

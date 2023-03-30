
const config = require('../setup/config');
const Stripe = require('stripe');

const stripe = Stripe(config.stripe.secretKey);

function convertExtraOptions(__extra) {
  var extraOptions = null;
  if (__extra && typeof __extra == "object" && Object.keys(__extra).length) {
    extraOptions = {};
    for (var option in __extra) {
      extraOptions[toCamelCase(option)] = __extra[option];
    }
  }
  return extraOptions;
}

function toCamelCase(str) {
  if (str == null) return str;
  return String(str)
      .toLowerCase()
      .replace(/[\s_]+(\S)/g, function(a, b) {
        return b.toUpperCase()
      });
}


// /v1/3d_secure - post
exports.createThreeDsecure = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.threeDSecure.create(options,__extra);
};

// /v1/3d_secure/{three_d_secure} - get
exports.retrieveThreeDsecure = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const three_d_secure = this.parseRequired(options.three_d_secure, 'string', 'stripe.retrieveThreeDsecure: three_d_secure is required.');
  delete options.three_d_secure;
  return stripe.threeDSecure.retrieve(three_d_secure, options,__extra);
};

// /v1/account_links - post
exports.createAccountLink = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.accountLinks.create(options,__extra);
};

// /v1/accounts - get
exports.listAccounts = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.accounts.list(options,__extra);
};

// /v1/accounts - post
exports.createAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.accounts.create(options,__extra);
};

// /v1/accounts/{account} - delete
exports.deleteAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.deleteAccount: account is required.');
  delete options.account;
  return stripe.accounts.del(account, options,__extra);
};

// /v1/accounts/{account} - get
exports.retrieveAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.retrieveAccount: account is required.');
  delete options.account;
  return stripe.accounts.retrieve(account, options,__extra);
};

// /v1/accounts/{account} - post
exports.updateAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.updateAccount: account is required.');
  delete options.account;
  return stripe.accounts.update(account, options,__extra);
};

// /v1/accounts/{account}/capabilities - get
exports.listAccountCapabilities = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.listAccountCapabilities: account is required.');
  delete options.account;
  return stripe.accounts.listCapabilities(account, options,__extra);
};

// /v1/accounts/{account}/capabilities/{capability} - get
exports.retrieveAccountCapabilitie = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.retrieveAccountCapabilitie: account is required.');
  delete options.account;
  const capability = this.parseRequired(options.capability, 'string', 'stripe.retrieveAccountCapabilitie: capability is required.');
  delete options.capability;
  return stripe.accounts.retrieveCapabilitie(account, capability, options,__extra);
};

// /v1/accounts/{account}/capabilities/{capability} - post
exports.updateAccountCapabilitie = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.updateAccountCapabilitie: account is required.');
  delete options.account;
  const capability = this.parseRequired(options.capability, 'string', 'stripe.updateAccountCapabilitie: capability is required.');
  delete options.capability;
  return stripe.accounts.updateCapabilitie(account, capability, options,__extra);
};

// /v1/accounts/{account}/external_accounts - get
exports.listAccountExternalAccounts = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.listAccountExternalAccounts: account is required.');
  delete options.account;
  return stripe.accounts.listExternalAccounts(account, options,__extra);
};

// /v1/accounts/{account}/external_accounts - post
exports.createAccountExternalAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.createAccountExternalAccount: account is required.');
  delete options.account;
  return stripe.accounts.createExternalAccount(account, options,__extra);
};

// /v1/accounts/{account}/external_accounts/{id} - delete
exports.deleteAccountExternalAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.deleteAccountExternalAccount: account is required.');
  delete options.account;
  const id = this.parseRequired(options.id, 'string', 'stripe.deleteAccountExternalAccount: id is required.');
  delete options.id;
  return stripe.accounts.deleteExternalAccount(account, id, options,__extra);
};

// /v1/accounts/{account}/external_accounts/{id} - get
exports.retrieveAccountExternalAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.retrieveAccountExternalAccount: account is required.');
  delete options.account;
  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveAccountExternalAccount: id is required.');
  delete options.id;
  return stripe.accounts.retrieveExternalAccount(account, id, options,__extra);
};

// /v1/accounts/{account}/external_accounts/{id} - post
exports.updateAccountExternalAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.updateAccountExternalAccount: account is required.');
  delete options.account;
  const id = this.parseRequired(options.id, 'string', 'stripe.updateAccountExternalAccount: id is required.');
  delete options.id;
  return stripe.accounts.updateExternalAccount(account, id, options,__extra);
};

// /v1/accounts/{account}/login_links - post
exports.createAccountLoginLink = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.createAccountLoginLink: account is required.');
  delete options.account;
  return stripe.accounts.createLoginLink(account, options,__extra);
};

// /v1/accounts/{account}/persons - get
exports.listAccountPersons = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.listAccountPersons: account is required.');
  delete options.account;
  return stripe.accounts.listPersons(account, options,__extra);
};

// /v1/accounts/{account}/persons - post
exports.createAccountPerson = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.createAccountPerson: account is required.');
  delete options.account;
  return stripe.accounts.createPerson(account, options,__extra);
};

// /v1/accounts/{account}/persons/{person} - delete
exports.deleteAccountPerson = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.deleteAccountPerson: account is required.');
  delete options.account;
  const person = this.parseRequired(options.person, 'string', 'stripe.deleteAccountPerson: person is required.');
  delete options.person;
  return stripe.accounts.deletePerson(account, person, options,__extra);
};

// /v1/accounts/{account}/persons/{person} - get
exports.retrieveAccountPerson = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.retrieveAccountPerson: account is required.');
  delete options.account;
  const person = this.parseRequired(options.person, 'string', 'stripe.retrieveAccountPerson: person is required.');
  delete options.person;
  return stripe.accounts.retrievePerson(account, person, options,__extra);
};

// /v1/accounts/{account}/persons/{person} - post
exports.updateAccountPerson = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.updateAccountPerson: account is required.');
  delete options.account;
  const person = this.parseRequired(options.person, 'string', 'stripe.updateAccountPerson: person is required.');
  delete options.person;
  return stripe.accounts.updatePerson(account, person, options,__extra);
};

// /v1/accounts/{account}/reject - post
exports.rejectAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.rejectAccount: account is required.');
  delete options.account;
  return stripe.accounts.reject(account, options,__extra);
};

// /v1/accounts/{account}/x-stripeParametersOverride_bank_account/{id} - post
exports.updateAccountXStripeParametersOverrideBankAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.updateAccountXStripeParametersOverrideBankAccount: account is required.');
  delete options.account;
  const id = this.parseRequired(options.id, 'string', 'stripe.updateAccountXStripeParametersOverrideBankAccount: id is required.');
  delete options.id;
  return stripe.accounts.updateXStripeParametersOverrideBankAccount(account, id, options,__extra);
};

// /v1/accounts/{account}/x-stripeParametersOverride_card/{id} - post
exports.updateAccountXStripeParametersOverrideCard = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.updateAccountXStripeParametersOverrideCard: account is required.');
  delete options.account;
  const id = this.parseRequired(options.id, 'string', 'stripe.updateAccountXStripeParametersOverrideCard: id is required.');
  delete options.id;
  return stripe.accounts.updateXStripeParametersOverrideCard(account, id, options,__extra);
};

// /v1/apple_pay/domains - get
exports.listApplePayDomains = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.applePay.domains.list(options,__extra);
};

// /v1/apple_pay/domains - post
exports.createApplePayDomain = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.applePay.domains.create(options,__extra);
};

// /v1/apple_pay/domains/{domain} - delete
exports.deleteApplePayDomain = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const domain = this.parseRequired(options.domain, 'string', 'stripe.deleteApplePayDomain: domain is required.');
  delete options.domain;
  return stripe.applePay.domains.del(domain, options,__extra);
};

// /v1/apple_pay/domains/{domain} - get
exports.retrieveApplePayDomain = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const domain = this.parseRequired(options.domain, 'string', 'stripe.retrieveApplePayDomain: domain is required.');
  delete options.domain;
  return stripe.applePay.domains.retrieve(domain, options,__extra);
};

// /v1/application_fees - get
exports.listApplicationFees = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.applicationFees.list(options,__extra);
};

// /v1/application_fees/{fee}/refunds/{id} - get
exports.retrieveApplicationFeeRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const fee = this.parseRequired(options.fee, 'string', 'stripe.retrieveApplicationFeeRefund: fee is required.');
  delete options.fee;
  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveApplicationFeeRefund: id is required.');
  delete options.id;
  return stripe.applicationFees.retrieveRefund(fee, id, options,__extra);
};

// /v1/application_fees/{fee}/refunds/{id} - post
exports.updateApplicationFeeRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const fee = this.parseRequired(options.fee, 'string', 'stripe.updateApplicationFeeRefund: fee is required.');
  delete options.fee;
  const id = this.parseRequired(options.id, 'string', 'stripe.updateApplicationFeeRefund: id is required.');
  delete options.id;
  return stripe.applicationFees.updateRefund(fee, id, options,__extra);
};

// /v1/application_fees/{id} - get
exports.retrieveApplicationFee = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveApplicationFee: id is required.');
  delete options.id;
  return stripe.applicationFees.retrieve(id, options,__extra);
};

// /v1/application_fees/{id}/refunds - get
exports.listApplicationFeeRefunds = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.listApplicationFeeRefunds: id is required.');
  delete options.id;
  return stripe.applicationFees.listRefunds(id, options,__extra);
};

// /v1/application_fees/{id}/refunds - post
exports.createApplicationFeeRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.createApplicationFeeRefund: id is required.');
  delete options.id;
  return stripe.applicationFees.createRefund(id, options,__extra);
};

// /v1/balance - get
exports.retrieveBalance = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.balance.retrieve(options,__extra);
};

// /v1/balance_transactions - get
exports.listBalanceTransactions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.balanceTransactions.list(options,__extra);
};

// /v1/balance_transactions/{id} - get
exports.retrieveBalanceTransaction = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveBalanceTransaction: id is required.');
  delete options.id;
  return stripe.balanceTransactions.retrieve(id, options,__extra);
};

// /v1/billing_portal/configurations - get
exports.listBillingPortalConfigurations = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.billingPortal.configurations.list(options,__extra);
};

// /v1/billing_portal/configurations - post
exports.createBillingPortalConfiguration = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.billingPortal.configurations.create(options,__extra);
};

// /v1/billing_portal/configurations/{configuration} - get
exports.retrieveBillingPortalConfiguration = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const configuration = this.parseRequired(options.configuration, 'string', 'stripe.retrieveBillingPortalConfiguration: configuration is required.');
  delete options.configuration;
  return stripe.billingPortal.configurations.retrieve(configuration, options,__extra);
};

// /v1/billing_portal/configurations/{configuration} - post
exports.updateBillingPortalConfiguration = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const configuration = this.parseRequired(options.configuration, 'string', 'stripe.updateBillingPortalConfiguration: configuration is required.');
  delete options.configuration;
  return stripe.billingPortal.configurations.update(configuration, options,__extra);
};

// /v1/billing_portal/sessions - post
exports.createBillingPortalSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.billingPortal.sessions.create(options,__extra);
};

// /v1/bitcoin/receivers - get
exports.listBitcoinReceivers = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.bitcoin.receivers.list(options,__extra);
};

// /v1/bitcoin/receivers/{id} - get
exports.retrieveBitcoinReceiver = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveBitcoinReceiver: id is required.');
  delete options.id;
  return stripe.bitcoin.receivers.retrieve(id, options,__extra);
};

// /v1/bitcoin/receivers/{receiver}/transactions - get
exports.listBitcoinReceiverTransactions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const receiver = this.parseRequired(options.receiver, 'string', 'stripe.listBitcoinReceiverTransactions: receiver is required.');
  delete options.receiver;
  return stripe.bitcoin.receivers.listTransactions(receiver, options,__extra);
};

// /v1/charges - get
exports.listCharges = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.charges.list(options,__extra);
};

// /v1/charges - post
exports.createCharge = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.charges.create(options,__extra);
};

// /v1/charges/search - get
exports.searchCharges = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const query = this.parseRequired(options.query, 'string', 'stripe.searchCharges: query is required.');
  return stripe.charges.search(options,__extra);
};

// /v1/charges/{charge} - get
exports.retrieveCharge = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const charge = this.parseRequired(options.charge, 'string', 'stripe.retrieveCharge: charge is required.');
  delete options.charge;
  return stripe.charges.retrieve(charge, options,__extra);
};

// /v1/charges/{charge} - post
exports.updateCharge = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const charge = this.parseRequired(options.charge, 'string', 'stripe.updateCharge: charge is required.');
  delete options.charge;
  return stripe.charges.update(charge, options,__extra);
};

// /v1/charges/{charge}/capture - post
exports.captureCharge = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const charge = this.parseRequired(options.charge, 'string', 'stripe.captureCharge: charge is required.');
  delete options.charge;
  return stripe.charges.capture(charge, options,__extra);
};

// /v1/charges/{charge}/refunds - get
exports.listChargeRefunds = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const charge = this.parseRequired(options.charge, 'string', 'stripe.listChargeRefunds: charge is required.');
  delete options.charge;
  return stripe.charges.listRefunds(charge, options,__extra);
};

// /v1/charges/{charge}/refunds/{refund} - get
exports.retrieveChargeRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const charge = this.parseRequired(options.charge, 'string', 'stripe.retrieveChargeRefund: charge is required.');
  delete options.charge;
  const refund = this.parseRequired(options.refund, 'string', 'stripe.retrieveChargeRefund: refund is required.');
  delete options.refund;
  return stripe.charges.retrieveRefund(charge, refund, options,__extra);
};

// /v1/checkout/sessions - get
exports.listCheckoutSessions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.checkout.sessions.list(options,__extra);
};

// /v1/checkout/sessions - post
exports.createCheckoutSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  if (options && options.lineItemsType) {
    if (options.lineItemsType == 'customList' || options.lineItemsType == 'customRef') {
      if (options.line_items) {
        if (!Array.isArray(options.line_items)) {
          if (typeof options.line_items == "object") {
            options.line_items = [options.line_items];
          } else {
            throw new Error('createCheckoutSession: line_items is not an array or object for references');
          }
        } else if (!options.line_items || options.line_items.length == 0) {
          throw new Error('createCheckoutSession: line_items is empty!');
        }
      } else {
        throw new Error('createCheckoutSession: line_items is not set!');
      }
      options.line_items = options.line_items.map(item => {
        return {
          price_data: {
            currency: item.currency ? item.currency : 'USD',
            product_data: {
              name: item.title,
            },
            unit_amount_decimal: item.amount,
          },
          quantity: item.quantity ? item.quantity : 1,
        }
      })
    }
    delete options.lineItemsType;
  } else {
    if (options.line_items) {
      if (Array.isArray(options.line_items)) {
        if (options.line_items.length == 0) {
          throw new Error('createCheckoutSession: line_items is empty!');
        }
        options.line_items = options.line_items.map(item => {
          return {
            price: item.price,
            quantity: item.quantity ? item.quantity : 1
          }
        })
      } else if (typeof options.line_items == "object") {
        options.line_items = [options.line_items]
      } else if (typeof options.line_items == "string") {
        options.line_items = [{price: options.line_items, quantity: 1}]
      }
    }
  }

  return stripe.checkout.sessions.create(options,__extra);
};

// /v1/checkout/sessions/{session} - get
exports.retrieveCheckoutSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const session = this.parseRequired(options.session, 'string', 'stripe.retrieveCheckoutSession: session is required.');
  delete options.session;
  return stripe.checkout.sessions.retrieve(session, options,__extra);
};

// /v1/checkout/sessions/{session}/expire - post
exports.expireCheckoutSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const session = this.parseRequired(options.session, 'string', 'stripe.expireCheckoutSession: session is required.');
  delete options.session;
  return stripe.checkout.sessions.expire(session, options,__extra);
};

// /v1/checkout/sessions/{session}/line_items - get
exports.listCheckoutSessionLineItems = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const session = this.parseRequired(options.session, 'string', 'stripe.listCheckoutSessionLineItems: session is required.');
  delete options.session;
  return stripe.checkout.sessions.listLineItems(session, options,__extra);
};

// /v1/country_specs - get
exports.listCountrySpecs = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.countrySpecs.list(options,__extra);
};

// /v1/country_specs/{country} - get
exports.retrieveCountrySpec = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const country = this.parseRequired(options.country, 'string', 'stripe.retrieveCountrySpec: country is required.');
  delete options.country;
  return stripe.countrySpecs.retrieve(country, options,__extra);
};

// /v1/coupons - get
exports.listCoupons = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.coupons.list(options,__extra);
};

// /v1/coupons - post
exports.createCoupon = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.coupons.create(options,__extra);
};

// /v1/coupons/{coupon} - delete
exports.deleteCoupon = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const coupon = this.parseRequired(options.coupon, 'string', 'stripe.deleteCoupon: coupon is required.');
  delete options.coupon;
  return stripe.coupons.del(coupon, options,__extra);
};

// /v1/coupons/{coupon} - get
exports.retrieveCoupon = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const coupon = this.parseRequired(options.coupon, 'string', 'stripe.retrieveCoupon: coupon is required.');
  delete options.coupon;
  return stripe.coupons.retrieve(coupon, options,__extra);
};

// /v1/coupons/{coupon} - post
exports.updateCoupon = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const coupon = this.parseRequired(options.coupon, 'string', 'stripe.updateCoupon: coupon is required.');
  delete options.coupon;
  return stripe.coupons.update(coupon, options,__extra);
};

// /v1/credit_notes - get
exports.listCreditNotes = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.creditNotes.list(options,__extra);
};

// /v1/credit_notes - post
exports.createCreditNote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.creditNotes.create(options,__extra);
};

// /v1/credit_notes/preview - get
exports.retrieveCreditNotesPreview = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.retrieveCreditNotesPreview: invoice is required.');
  return stripe.creditNotes.preview(options,__extra);
};

// /v1/credit_notes/preview/lines - get
exports.listCreditNotesPreviewLines = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.listCreditNotesPreviewLines: invoice is required.');
  return stripe.creditNotes.listPreviewLineItems(options,__extra);
};

// /v1/credit_notes/{credit_note}/lines - get
exports.listCreditNoteLines = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const credit_note = this.parseRequired(options.credit_note, 'string', 'stripe.listCreditNoteLines: credit_note is required.');
  delete options.credit_note;
  return stripe.creditNotes.listLines(credit_note, options,__extra);
};

// /v1/credit_notes/{id} - get
exports.retrieveCreditNote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveCreditNote: id is required.');
  delete options.id;
  return stripe.creditNotes.retrieve(id, options,__extra);
};

// /v1/credit_notes/{id} - post
exports.updateCreditNote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.updateCreditNote: id is required.');
  delete options.id;
  return stripe.creditNotes.update(id, options,__extra);
};

// /v1/credit_notes/{id}/void - post
exports.voidCreditNote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.voidCreditNote: id is required.');
  delete options.id;
  return stripe.creditNotes.voidCreditNote(id, options,__extra);
};

// /v1/customers - get
exports.listCustomers = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.customers.list(options,__extra);
};

// /v1/customers - post
exports.createCustomer = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.customers.create(options,__extra);
};

// /v1/customers/search - get
exports.searchCustomers = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const query = this.parseRequired(options.query, 'string', 'stripe.searchCustomers: query is required.');
  return stripe.customers.search(options,__extra);
};

// /v1/customers/{customer} - delete
exports.deleteCustomer = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.deleteCustomer: customer is required.');
  delete options.customer;
  return stripe.customers.del(customer, options,__extra);
};

// /v1/customers/{customer} - get
exports.retrieveCustomer = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.retrieveCustomer: customer is required.');
  delete options.customer;
  return stripe.customers.retrieve(customer, options,__extra);
};

// /v1/customers/{customer} - post
exports.updateCustomer = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.updateCustomer: customer is required.');
  delete options.customer;
  return stripe.customers.update(customer, options,__extra);
};

// /v1/customers/{customer}/balance_transactions - get
exports.listCustomerBalanceTransactions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.listCustomerBalanceTransactions: customer is required.');
  delete options.customer;
  return stripe.customers.listBalanceTransactions(customer, options,__extra);
};

// /v1/customers/{customer}/balance_transactions - post
exports.createCustomerBalanceTransaction = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.createCustomerBalanceTransaction: customer is required.');
  delete options.customer;
  return stripe.customers.createBalanceTransaction(customer, options,__extra);
};

// /v1/customers/{customer}/balance_transactions/{transaction} - get
exports.retrieveCustomerBalanceTransaction = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.retrieveCustomerBalanceTransaction: customer is required.');
  delete options.customer;
  const transaction = this.parseRequired(options.transaction, 'string', 'stripe.retrieveCustomerBalanceTransaction: transaction is required.');
  delete options.transaction;
  return stripe.customers.retrieveBalanceTransaction(customer, transaction, options,__extra);
};

// /v1/customers/{customer}/balance_transactions/{transaction} - post
exports.updateCustomerBalanceTransaction = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.updateCustomerBalanceTransaction: customer is required.');
  delete options.customer;
  const transaction = this.parseRequired(options.transaction, 'string', 'stripe.updateCustomerBalanceTransaction: transaction is required.');
  delete options.transaction;
  return stripe.customers.updateBalanceTransaction(customer, transaction, options,__extra);
};

// /v1/customers/{customer}/cash_balance - get
exports.retrieveCustomerCashBalance = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.retrieveCustomerCashBalance: customer is required.');
  delete options.customer;
  return stripe.customers.retrieveCashBalance(customer, options,__extra);
};

// /v1/customers/{customer}/cash_balance - post
exports.cashBalanceCustomer = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.cashBalanceCustomer: customer is required.');
  delete options.customer;
  return stripe.customers.cashBalance(customer, options,__extra);
};

// /v1/customers/{customer}/discount - delete
exports.deleteCustomerDiscount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.deleteCustomerDiscount: customer is required.');
  delete options.customer;
  return stripe.customers.deleteDiscount(customer, options,__extra);
};

// /v1/customers/{customer}/funding_instructions - post
exports.createCustomerFundingInstruction = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.createCustomerFundingInstruction: customer is required.');
  delete options.customer;
  return stripe.customers.createFundingInstruction(customer, options,__extra);
};

// /v1/customers/{customer}/payment_methods - get
exports.listCustomerPaymentMethods = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.listCustomerPaymentMethods: customer is required.');
  delete options.customer;
  const type = this.parseRequired(options.type, 'string', 'stripe.listCustomerPaymentMethods: type is required.');
  return stripe.customers.listPaymentMethods(customer, options,__extra);
};

// /v1/customers/{customer}/sources - get
exports.listCustomerSources = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.listCustomerSources: customer is required.');
  delete options.customer;
  return stripe.customers.listSources(customer, options,__extra);
};

// /v1/customers/{customer}/sources - post
exports.createCustomerSource = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.createCustomerSource: customer is required.');
  delete options.customer;
  return stripe.customers.createSource(customer, options,__extra);
};

// /v1/customers/{customer}/sources/{id} - delete
exports.deleteCustomerSource = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.deleteCustomerSource: customer is required.');
  delete options.customer;
  const id = this.parseRequired(options.id, 'string', 'stripe.deleteCustomerSource: id is required.');
  delete options.id;
  return stripe.customers.deleteSource(customer, id, options,__extra);
};

// /v1/customers/{customer}/sources/{id} - get
exports.retrieveCustomerSource = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.retrieveCustomerSource: customer is required.');
  delete options.customer;
  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveCustomerSource: id is required.');
  delete options.id;
  return stripe.customers.retrieveSource(customer, id, options,__extra);
};

// /v1/customers/{customer}/sources/{id} - post
exports.updateCustomerSource = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.updateCustomerSource: customer is required.');
  delete options.customer;
  const id = this.parseRequired(options.id, 'string', 'stripe.updateCustomerSource: id is required.');
  delete options.id;
  return stripe.customers.updateSource(customer, id, options,__extra);
};

// /v1/customers/{customer}/tax_ids - get
exports.listCustomerTaxIds = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.listCustomerTaxIds: customer is required.');
  delete options.customer;
  return stripe.customers.listTaxIds(customer, options,__extra);
};

// /v1/customers/{customer}/tax_ids - post
exports.createCustomerTaxId = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.createCustomerTaxId: customer is required.');
  delete options.customer;
  return stripe.customers.createTaxId(customer, options,__extra);
};

// /v1/customers/{customer}/tax_ids/{id} - delete
exports.deleteCustomerTaxId = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.deleteCustomerTaxId: customer is required.');
  delete options.customer;
  const id = this.parseRequired(options.id, 'string', 'stripe.deleteCustomerTaxId: id is required.');
  delete options.id;
  return stripe.customers.deleteTaxId(customer, id, options,__extra);
};

// /v1/customers/{customer}/tax_ids/{id} - get
exports.retrieveCustomerTaxId = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.retrieveCustomerTaxId: customer is required.');
  delete options.customer;
  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveCustomerTaxId: id is required.');
  delete options.id;
  return stripe.customers.retrieveTaxId(customer, id, options,__extra);
};

// /v1/customers/{customer}/x-stripeParametersOverride_bank_accounts/{id} - post
exports.updateCustomerXStripeParametersOverrideBankAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.updateCustomerXStripeParametersOverrideBankAccount: customer is required.');
  delete options.customer;
  const id = this.parseRequired(options.id, 'string', 'stripe.updateCustomerXStripeParametersOverrideBankAccount: id is required.');
  delete options.id;
  return stripe.customers.updateXStripeParametersOverrideBankAccount(customer, id, options,__extra);
};

// /v1/customers/{customer}/x-stripeParametersOverride_cards/{id} - post
exports.updateCustomerXStripeParametersOverrideCard = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const customer = this.parseRequired(options.customer, 'string', 'stripe.updateCustomerXStripeParametersOverrideCard: customer is required.');
  delete options.customer;
  const id = this.parseRequired(options.id, 'string', 'stripe.updateCustomerXStripeParametersOverrideCard: id is required.');
  delete options.id;
  return stripe.customers.updateXStripeParametersOverrideCard(customer, id, options,__extra);
};

// /v1/disputes - get
exports.listDisputes = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.disputes.list(options,__extra);
};

// /v1/disputes/{dispute} - get
exports.retrieveDispute = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const dispute = this.parseRequired(options.dispute, 'string', 'stripe.retrieveDispute: dispute is required.');
  delete options.dispute;
  return stripe.disputes.retrieve(dispute, options,__extra);
};

// /v1/disputes/{dispute} - post
exports.updateDispute = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const dispute = this.parseRequired(options.dispute, 'string', 'stripe.updateDispute: dispute is required.');
  delete options.dispute;
  return stripe.disputes.update(dispute, options,__extra);
};

// /v1/disputes/{dispute}/close - post
exports.closeDispute = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const dispute = this.parseRequired(options.dispute, 'string', 'stripe.closeDispute: dispute is required.');
  delete options.dispute;
  return stripe.disputes.close(dispute, options,__extra);
};

// /v1/ephemeral_keys - post
exports.createEphemeralKey = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.ephemeralKeys.create(options,__extra);
};

// /v1/ephemeral_keys/{key} - delete
exports.deleteEphemeralKey = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const key = this.parseRequired(options.key, 'string', 'stripe.deleteEphemeralKey: key is required.');
  delete options.key;
  return stripe.ephemeralKeys.del(key, options,__extra);
};

// /v1/events - get
exports.listEvents = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.events.list(options,__extra);
};

// /v1/events/{id} - get
exports.retrieveEvent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveEvent: id is required.');
  delete options.id;
  return stripe.events.retrieve(id, options,__extra);
};

// /v1/exchange_rates - get
exports.listExchangeRates = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.exchangeRates.list(options,__extra);
};

// /v1/exchange_rates/{rate_id} - get
exports.retrieveExchangeRate = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const rate_id = this.parseRequired(options.rate_id, 'string', 'stripe.retrieveExchangeRate: rate_id is required.');
  delete options.rate_id;
  return stripe.exchangeRates.retrieve(rate_id, options,__extra);
};

// /v1/file_links - get
exports.listFileLinks = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.fileLinks.list(options,__extra);
};

// /v1/file_links - post
exports.createFileLink = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.fileLinks.create(options,__extra);
};

// /v1/file_links/{link} - get
exports.retrieveFileLink = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const link = this.parseRequired(options.link, 'string', 'stripe.retrieveFileLink: link is required.');
  delete options.link;
  return stripe.fileLinks.retrieve(link, options,__extra);
};

// /v1/file_links/{link} - post
exports.updateFileLink = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const link = this.parseRequired(options.link, 'string', 'stripe.updateFileLink: link is required.');
  delete options.link;
  return stripe.fileLinks.update(link, options,__extra);
};

// /v1/files - get
exports.listFiles = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.files.list(options,__extra);
};

// /v1/files - post
exports.createFile = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.files.create(options,__extra);
};

// /v1/files/{file} - get
exports.retrieveFile = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const file = this.parseRequired(options.file, 'string', 'stripe.retrieveFile: file is required.');
  delete options.file;
  return stripe.files.retrieve(file, options,__extra);
};

// /v1/financial_connections/accounts/{account} - get
exports.retrieveFinancialConnectionsAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.retrieveFinancialConnectionsAccount: account is required.');
  delete options.account;
  return stripe.financialConnections.accounts.retrieve(account, options,__extra);
};

// /v1/financial_connections/accounts/{account}/disconnect - post
exports.disconnectFinancialConnectionsAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.disconnectFinancialConnectionsAccount: account is required.');
  delete options.account;
  return stripe.financialConnections.accounts.disconnect(account, options,__extra);
};

// /v1/financial_connections/accounts/{account}/refresh - post
exports.refreshFinancialConnectionsAccount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const account = this.parseRequired(options.account, 'string', 'stripe.refreshFinancialConnectionsAccount: account is required.');
  delete options.account;
  return stripe.financialConnections.accounts.refresh(account, options,__extra);
};

// /v1/financial_connections/sessions - post
exports.createFinancialConnectionsSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.financialConnections.sessions.create(options,__extra);
};

// /v1/financial_connections/sessions/{session} - get
exports.retrieveFinancialConnectionsSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const session = this.parseRequired(options.session, 'string', 'stripe.retrieveFinancialConnectionsSession: session is required.');
  delete options.session;
  return stripe.financialConnections.sessions.retrieve(session, options,__extra);
};

// /v1/identity/verification_reports - get
exports.listIdentityVerificationReports = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.identity.verificationReports.list(options,__extra);
};

// /v1/identity/verification_reports/{report} - get
exports.retrieveIdentityVerificationReport = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const report = this.parseRequired(options.report, 'string', 'stripe.retrieveIdentityVerificationReport: report is required.');
  delete options.report;
  return stripe.identity.verificationReports.retrieve(report, options,__extra);
};

// /v1/identity/verification_sessions - get
exports.listIdentityVerificationSessions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.identity.verificationSessions.list(options,__extra);
};

// /v1/identity/verification_sessions - post
exports.createIdentityVerificationSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.identity.verificationSessions.create(options,__extra);
};

// /v1/identity/verification_sessions/{session} - get
exports.retrieveIdentityVerificationSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const session = this.parseRequired(options.session, 'string', 'stripe.retrieveIdentityVerificationSession: session is required.');
  delete options.session;
  return stripe.identity.verificationSessions.retrieve(session, options,__extra);
};

// /v1/identity/verification_sessions/{session} - post
exports.updateIdentityVerificationSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const session = this.parseRequired(options.session, 'string', 'stripe.updateIdentityVerificationSession: session is required.');
  delete options.session;
  return stripe.identity.verificationSessions.update(session, options,__extra);
};

// /v1/identity/verification_sessions/{session}/cancel - post
exports.cancelIdentityVerificationSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const session = this.parseRequired(options.session, 'string', 'stripe.cancelIdentityVerificationSession: session is required.');
  delete options.session;
  return stripe.identity.verificationSessions.cancel(session, options,__extra);
};

// /v1/identity/verification_sessions/{session}/redact - post
exports.redactIdentityVerificationSession = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const session = this.parseRequired(options.session, 'string', 'stripe.redactIdentityVerificationSession: session is required.');
  delete options.session;
  return stripe.identity.verificationSessions.redact(session, options,__extra);
};

// /v1/invoiceitems - get
exports.listInvoiceitems = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.invoiceitems.list(options,__extra);
};

// /v1/invoiceitems - post
exports.createInvoiceitem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.invoiceitems.create(options,__extra);
};

// /v1/invoiceitems/{invoiceitem} - delete
exports.deleteInvoiceitem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoiceitem = this.parseRequired(options.invoiceitem, 'string', 'stripe.deleteInvoiceitem: invoiceitem is required.');
  delete options.invoiceitem;
  return stripe.invoiceitems.del(invoiceitem, options,__extra);
};

// /v1/invoiceitems/{invoiceitem} - get
exports.retrieveInvoiceitem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoiceitem = this.parseRequired(options.invoiceitem, 'string', 'stripe.retrieveInvoiceitem: invoiceitem is required.');
  delete options.invoiceitem;
  return stripe.invoiceitems.retrieve(invoiceitem, options,__extra);
};

// /v1/invoiceitems/{invoiceitem} - post
exports.updateInvoiceitem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoiceitem = this.parseRequired(options.invoiceitem, 'string', 'stripe.updateInvoiceitem: invoiceitem is required.');
  delete options.invoiceitem;
  return stripe.invoiceitems.update(invoiceitem, options,__extra);
};

// /v1/invoices - get
exports.listInvoices = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.invoices.list(options,__extra);
};

// /v1/invoices - post
exports.createInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.invoices.create(options,__extra);
};

// /v1/invoices/search - get
exports.searchInvoices = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const query = this.parseRequired(options.query, 'string', 'stripe.searchInvoices: query is required.');
  return stripe.invoices.search(options,__extra);
};

// /v1/invoices/upcoming - get
exports.retrieveInvoicesUpcoming = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.invoices.retrieveUpcoming(options,__extra);
};

// /v1/invoices/upcoming/lines - get
exports.listInvoicesUpcomingLines = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.invoices.listUpcomingLineItems(options,__extra);
};

// /v1/invoices/{invoice} - delete
exports.deleteInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.deleteInvoice: invoice is required.');
  delete options.invoice;
  return stripe.invoices.del(invoice, options,__extra);
};

// /v1/invoices/{invoice} - get
exports.retrieveInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.retrieveInvoice: invoice is required.');
  delete options.invoice;
  return stripe.invoices.retrieve(invoice, options,__extra);
};

// /v1/invoices/{invoice} - post
exports.updateInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.updateInvoice: invoice is required.');
  delete options.invoice;
  return stripe.invoices.update(invoice, options,__extra);
};

// /v1/invoices/{invoice}/finalize - post
exports.finalizeInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.finalizeInvoice: invoice is required.');
  delete options.invoice;
  return stripe.invoices.finalizeInvoice(invoice, options,__extra);
};

// /v1/invoices/{invoice}/lines - get
exports.listInvoiceLines = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.listInvoiceLines: invoice is required.');
  delete options.invoice;
  return stripe.invoices.listLines(invoice, options,__extra);
};

// /v1/invoices/{invoice}/mark_uncollectible - post
exports.markUncollectibleInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.markUncollectibleInvoice: invoice is required.');
  delete options.invoice;
  return stripe.invoices.markUncollectible(invoice, options,__extra);
};

// /v1/invoices/{invoice}/pay - post
exports.payInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.payInvoice: invoice is required.');
  delete options.invoice;
  return stripe.invoices.pay(invoice, options,__extra);
};

// /v1/invoices/{invoice}/send - post
exports.sendInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.sendInvoice: invoice is required.');
  delete options.invoice;
  return stripe.invoices.sendInvoice(invoice, options,__extra);
};

// /v1/invoices/{invoice}/void - post
exports.voidInvoice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const invoice = this.parseRequired(options.invoice, 'string', 'stripe.voidInvoice: invoice is required.');
  delete options.invoice;
  return stripe.invoices.voidInvoice(invoice, options,__extra);
};

// /v1/issuer_fraud_records - get
exports.listIssuerFraudRecords = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuerFraudRecords.list(options,__extra);
};

// /v1/issuer_fraud_records/{issuer_fraud_record} - get
exports.retrieveIssuerFraudRecord = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const issuer_fraud_record = this.parseRequired(options.issuer_fraud_record, 'string', 'stripe.retrieveIssuerFraudRecord: issuer_fraud_record is required.');
  delete options.issuer_fraud_record;
  return stripe.issuerFraudRecords.retrieve(issuer_fraud_record, options,__extra);
};

// /v1/issuing/authorizations - get
exports.listIssuingAuthorizations = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuing.authorizations.list(options,__extra);
};

// /v1/issuing/authorizations/{authorization} - get
exports.retrieveIssuingAuthorization = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const authorization = this.parseRequired(options.authorization, 'string', 'stripe.retrieveIssuingAuthorization: authorization is required.');
  delete options.authorization;
  return stripe.issuing.authorizations.retrieve(authorization, options,__extra);
};

// /v1/issuing/authorizations/{authorization} - post
exports.updateIssuingAuthorization = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const authorization = this.parseRequired(options.authorization, 'string', 'stripe.updateIssuingAuthorization: authorization is required.');
  delete options.authorization;
  return stripe.issuing.authorizations.update(authorization, options,__extra);
};

// /v1/issuing/authorizations/{authorization}/approve - post
exports.approveIssuingAuthorization = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const authorization = this.parseRequired(options.authorization, 'string', 'stripe.approveIssuingAuthorization: authorization is required.');
  delete options.authorization;
  return stripe.issuing.authorizations.approve(authorization, options,__extra);
};

// /v1/issuing/authorizations/{authorization}/decline - post
exports.declineIssuingAuthorization = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const authorization = this.parseRequired(options.authorization, 'string', 'stripe.declineIssuingAuthorization: authorization is required.');
  delete options.authorization;
  return stripe.issuing.authorizations.decline(authorization, options,__extra);
};

// /v1/issuing/cardholders - get
exports.listIssuingCardholders = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuing.cardholders.list(options,__extra);
};

// /v1/issuing/cardholders - post
exports.createIssuingCardholder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuing.cardholders.create(options,__extra);
};

// /v1/issuing/cardholders/{cardholder} - get
exports.retrieveIssuingCardholder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const cardholder = this.parseRequired(options.cardholder, 'string', 'stripe.retrieveIssuingCardholder: cardholder is required.');
  delete options.cardholder;
  return stripe.issuing.cardholders.retrieve(cardholder, options,__extra);
};

// /v1/issuing/cardholders/{cardholder} - post
exports.updateIssuingCardholder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const cardholder = this.parseRequired(options.cardholder, 'string', 'stripe.updateIssuingCardholder: cardholder is required.');
  delete options.cardholder;
  return stripe.issuing.cardholders.update(cardholder, options,__extra);
};

// /v1/issuing/cards - get
exports.listIssuingCards = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuing.cards.list(options,__extra);
};

// /v1/issuing/cards - post
exports.createIssuingCard = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuing.cards.create(options,__extra);
};

// /v1/issuing/cards/{card} - get
exports.retrieveIssuingCard = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const card = this.parseRequired(options.card, 'string', 'stripe.retrieveIssuingCard: card is required.');
  delete options.card;
  return stripe.issuing.cards.retrieve(card, options,__extra);
};

// /v1/issuing/cards/{card} - post
exports.updateIssuingCard = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const card = this.parseRequired(options.card, 'string', 'stripe.updateIssuingCard: card is required.');
  delete options.card;
  return stripe.issuing.cards.update(card, options,__extra);
};

// /v1/issuing/disputes - get
exports.listIssuingDisputes = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuing.disputes.list(options,__extra);
};

// /v1/issuing/disputes - post
exports.createIssuingDispute = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuing.disputes.create(options,__extra);
};

// /v1/issuing/disputes/{dispute} - get
exports.retrieveIssuingDispute = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const dispute = this.parseRequired(options.dispute, 'string', 'stripe.retrieveIssuingDispute: dispute is required.');
  delete options.dispute;
  return stripe.issuing.disputes.retrieve(dispute, options,__extra);
};

// /v1/issuing/disputes/{dispute} - post
exports.updateIssuingDispute = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const dispute = this.parseRequired(options.dispute, 'string', 'stripe.updateIssuingDispute: dispute is required.');
  delete options.dispute;
  return stripe.issuing.disputes.update(dispute, options,__extra);
};

// /v1/issuing/disputes/{dispute}/submit - post
exports.submitIssuingDispute = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const dispute = this.parseRequired(options.dispute, 'string', 'stripe.submitIssuingDispute: dispute is required.');
  delete options.dispute;
  return stripe.issuing.disputes.submit(dispute, options,__extra);
};

// /v1/issuing/transactions - get
exports.listIssuingTransactions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.issuing.transactions.list(options,__extra);
};

// /v1/issuing/transactions/{transaction} - get
exports.retrieveIssuingTransaction = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const transaction = this.parseRequired(options.transaction, 'string', 'stripe.retrieveIssuingTransaction: transaction is required.');
  delete options.transaction;
  return stripe.issuing.transactions.retrieve(transaction, options,__extra);
};

// /v1/issuing/transactions/{transaction} - post
exports.updateIssuingTransaction = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const transaction = this.parseRequired(options.transaction, 'string', 'stripe.updateIssuingTransaction: transaction is required.');
  delete options.transaction;
  return stripe.issuing.transactions.update(transaction, options,__extra);
};

// /v1/mandates/{mandate} - get
exports.retrieveMandate = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const mandate = this.parseRequired(options.mandate, 'string', 'stripe.retrieveMandate: mandate is required.');
  delete options.mandate;
  return stripe.mandates.retrieve(mandate, options,__extra);
};

// /v1/orders - get
exports.listOrders = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.orders.list(options,__extra);
};

// /v1/orders - post
exports.createOrder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.orders.create(options,__extra);
};

// /v1/orders/{id} - get
exports.retrieveOrder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveOrder: id is required.');
  delete options.id;
  return stripe.orders.retrieve(id, options,__extra);
};

// /v1/orders/{id} - post
exports.updateOrder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.updateOrder: id is required.');
  delete options.id;
  return stripe.orders.update(id, options,__extra);
};

// /v1/orders/{id}/cancel - post
exports.cancelOrder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.cancelOrder: id is required.');
  delete options.id;
  return stripe.orders.cancel(id, options,__extra);
};

// /v1/orders/{id}/line_items - get
exports.listOrderLineItems = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.listOrderLineItems: id is required.');
  delete options.id;
  return stripe.orders.listLineItems(id, options,__extra);
};

// /v1/orders/{id}/reopen - post
exports.reopenOrder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.reopenOrder: id is required.');
  delete options.id;
  return stripe.orders.reopen(id, options,__extra);
};

// /v1/orders/{id}/submit - post
exports.submitOrder = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.submitOrder: id is required.');
  delete options.id;
  return stripe.orders.submit(id, options,__extra);
};

// /v1/payment_intents - get
exports.listPaymentIntents = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.paymentIntents.list(options,__extra);
};

// /v1/payment_intents - post
exports.createPaymentIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.paymentIntents.create(options,__extra);
};

// /v1/payment_intents/search - get
exports.searchPaymentIntents = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const query = this.parseRequired(options.query, 'string', 'stripe.searchPaymentIntents: query is required.');
  return stripe.paymentIntents.search(options,__extra);
};

// /v1/payment_intents/{intent} - get
exports.retrievePaymentIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.retrievePaymentIntent: intent is required.');
  delete options.intent;
  return stripe.paymentIntents.retrieve(intent, options,__extra);
};

// /v1/payment_intents/{intent} - post
exports.updatePaymentIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.updatePaymentIntent: intent is required.');
  delete options.intent;
  return stripe.paymentIntents.update(intent, options,__extra);
};

// /v1/payment_intents/{intent}/apply_customer_balance - post
exports.applyCustomerBalancePaymentIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.applyCustomerBalancePaymentIntent: intent is required.');
  delete options.intent;
  return stripe.paymentIntents.applyCustomerBalance(intent, options,__extra);
};

// /v1/payment_intents/{intent}/cancel - post
exports.cancelPaymentIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.cancelPaymentIntent: intent is required.');
  delete options.intent;
  return stripe.paymentIntents.cancel(intent, options,__extra);
};

// /v1/payment_intents/{intent}/capture - post
exports.capturePaymentIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.capturePaymentIntent: intent is required.');
  delete options.intent;
  return stripe.paymentIntents.capture(intent, options,__extra);
};

// /v1/payment_intents/{intent}/confirm - post
exports.confirmPaymentIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.confirmPaymentIntent: intent is required.');
  delete options.intent;
  return stripe.paymentIntents.confirm(intent, options,__extra);
};

// /v1/payment_intents/{intent}/increment_authorization - post
exports.incrementAuthorizationPaymentIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.incrementAuthorizationPaymentIntent: intent is required.');
  delete options.intent;
  return stripe.paymentIntents.incrementAuthorization(intent, options,__extra);
};

// /v1/payment_intents/{intent}/verify_microdeposits - post
exports.createPaymentIntentVerifyMicrodeposit = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.createPaymentIntentVerifyMicrodeposit: intent is required.');
  delete options.intent;
  return stripe.paymentIntents.createVerifyMicrodeposit(intent, options,__extra);
};

// /v1/payment_links - get
exports.listPaymentLinks = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.paymentLinks.list(options,__extra);
};

// /v1/payment_links - post
exports.createPaymentLink = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.paymentLinks.create(options,__extra);
};

// /v1/payment_links/{payment_link} - get
exports.retrievePaymentLink = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payment_link = this.parseRequired(options.payment_link, 'string', 'stripe.retrievePaymentLink: payment_link is required.');
  delete options.payment_link;
  return stripe.paymentLinks.retrieve(payment_link, options,__extra);
};

// /v1/payment_links/{payment_link} - post
exports.updatePaymentLink = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payment_link = this.parseRequired(options.payment_link, 'string', 'stripe.updatePaymentLink: payment_link is required.');
  delete options.payment_link;
  return stripe.paymentLinks.update(payment_link, options,__extra);
};

// /v1/payment_links/{payment_link}/line_items - get
exports.listPaymentLinkLineItems = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payment_link = this.parseRequired(options.payment_link, 'string', 'stripe.listPaymentLinkLineItems: payment_link is required.');
  delete options.payment_link;
  return stripe.paymentLinks.listLineItems(payment_link, options,__extra);
};

// /v1/payment_methods - get
exports.listPaymentMethods = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const type = this.parseRequired(options.type, 'string', 'stripe.listPaymentMethods: type is required.');
  return stripe.paymentMethods.list(options,__extra);
};

// /v1/payment_methods - post
exports.createPaymentMethod = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.paymentMethods.create(options,__extra);
};

// /v1/payment_methods/{payment_method} - get
exports.retrievePaymentMethod = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payment_method = this.parseRequired(options.payment_method, 'string', 'stripe.retrievePaymentMethod: payment_method is required.');
  delete options.payment_method;
  return stripe.paymentMethods.retrieve(payment_method, options,__extra);
};

// /v1/payment_methods/{payment_method} - post
exports.updatePaymentMethod = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payment_method = this.parseRequired(options.payment_method, 'string', 'stripe.updatePaymentMethod: payment_method is required.');
  delete options.payment_method;
  return stripe.paymentMethods.update(payment_method, options,__extra);
};

// /v1/payment_methods/{payment_method}/attach - post
exports.attachPaymentMethod = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payment_method = this.parseRequired(options.payment_method, 'string', 'stripe.attachPaymentMethod: payment_method is required.');
  delete options.payment_method;
  return stripe.paymentMethods.attach(payment_method, options,__extra);
};

// /v1/payment_methods/{payment_method}/detach - post
exports.detachPaymentMethod = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payment_method = this.parseRequired(options.payment_method, 'string', 'stripe.detachPaymentMethod: payment_method is required.');
  delete options.payment_method;
  return stripe.paymentMethods.detach(payment_method, options,__extra);
};

// /v1/payouts - get
exports.listPayouts = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.payouts.list(options,__extra);
};

// /v1/payouts - post
exports.createPayout = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.payouts.create(options,__extra);
};

// /v1/payouts/{payout} - get
exports.retrievePayout = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payout = this.parseRequired(options.payout, 'string', 'stripe.retrievePayout: payout is required.');
  delete options.payout;
  return stripe.payouts.retrieve(payout, options,__extra);
};

// /v1/payouts/{payout} - post
exports.updatePayout = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payout = this.parseRequired(options.payout, 'string', 'stripe.updatePayout: payout is required.');
  delete options.payout;
  return stripe.payouts.update(payout, options,__extra);
};

// /v1/payouts/{payout}/cancel - post
exports.cancelPayout = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payout = this.parseRequired(options.payout, 'string', 'stripe.cancelPayout: payout is required.');
  delete options.payout;
  return stripe.payouts.cancel(payout, options,__extra);
};

// /v1/payouts/{payout}/reverse - post
exports.reversePayout = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const payout = this.parseRequired(options.payout, 'string', 'stripe.reversePayout: payout is required.');
  delete options.payout;
  return stripe.payouts.reverse(payout, options,__extra);
};

// /v1/plans - get
exports.listPlans = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.plans.list(options,__extra);
};

// /v1/plans - post
exports.createPlan = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.plans.create(options,__extra);
};

// /v1/plans/{plan} - delete
exports.deletePlan = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const plan = this.parseRequired(options.plan, 'string', 'stripe.deletePlan: plan is required.');
  delete options.plan;
  return stripe.plans.del(plan, options,__extra);
};

// /v1/plans/{plan} - get
exports.retrievePlan = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const plan = this.parseRequired(options.plan, 'string', 'stripe.retrievePlan: plan is required.');
  delete options.plan;
  return stripe.plans.retrieve(plan, options,__extra);
};

// /v1/plans/{plan} - post
exports.updatePlan = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const plan = this.parseRequired(options.plan, 'string', 'stripe.updatePlan: plan is required.');
  delete options.plan;
  return stripe.plans.update(plan, options,__extra);
};

// /v1/prices - get
exports.listPrices = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.prices.list(options,__extra);
};

// /v1/prices - post
exports.createPrice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.prices.create(options,__extra);
};

// /v1/prices/search - get
exports.searchPrices = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const query = this.parseRequired(options.query, 'string', 'stripe.searchPrices: query is required.');
  return stripe.prices.search(options,__extra);
};

// /v1/prices/{price} - get
exports.retrievePrice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const price = this.parseRequired(options.price, 'string', 'stripe.retrievePrice: price is required.');
  delete options.price;
  return stripe.prices.retrieve(price, options,__extra);
};

// /v1/prices/{price} - post
exports.updatePrice = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const price = this.parseRequired(options.price, 'string', 'stripe.updatePrice: price is required.');
  delete options.price;
  return stripe.prices.update(price, options,__extra);
};

// /v1/products - get
exports.listProducts = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.products.list(options,__extra);
};

// /v1/products - post
exports.createProduct = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.products.create(options,__extra);
};

// /v1/products/search - get
exports.searchProducts = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const query = this.parseRequired(options.query, 'string', 'stripe.searchProducts: query is required.');
  return stripe.products.search(options,__extra);
};

// /v1/products/{id} - delete
exports.deleteProduct = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.deleteProduct: id is required.');
  delete options.id;
  return stripe.products.del(id, options,__extra);
};

// /v1/products/{id} - get
exports.retrieveProduct = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveProduct: id is required.');
  delete options.id;
  return stripe.products.retrieve(id, options,__extra);
};

// /v1/products/{id} - post
exports.updateProduct = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.updateProduct: id is required.');
  delete options.id;
  return stripe.products.update(id, options,__extra);
};

// /v1/promotion_codes - get
exports.listPromotionCodes = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.promotionCodes.list(options,__extra);
};

// /v1/promotion_codes - post
exports.createPromotionCode = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.promotionCodes.create(options,__extra);
};

// /v1/promotion_codes/{promotion_code} - get
exports.retrievePromotionCode = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const promotion_code = this.parseRequired(options.promotion_code, 'string', 'stripe.retrievePromotionCode: promotion_code is required.');
  delete options.promotion_code;
  return stripe.promotionCodes.retrieve(promotion_code, options,__extra);
};

// /v1/promotion_codes/{promotion_code} - post
exports.updatePromotionCode = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const promotion_code = this.parseRequired(options.promotion_code, 'string', 'stripe.updatePromotionCode: promotion_code is required.');
  delete options.promotion_code;
  return stripe.promotionCodes.update(promotion_code, options,__extra);
};

// /v1/quotes - get
exports.listQuotes = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.quotes.list(options,__extra);
};

// /v1/quotes - post
exports.createQuote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.quotes.create(options,__extra);
};

// /v1/quotes/{quote} - get
exports.retrieveQuote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const quote = this.parseRequired(options.quote, 'string', 'stripe.retrieveQuote: quote is required.');
  delete options.quote;
  return stripe.quotes.retrieve(quote, options,__extra);
};

// /v1/quotes/{quote} - post
exports.updateQuote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const quote = this.parseRequired(options.quote, 'string', 'stripe.updateQuote: quote is required.');
  delete options.quote;
  return stripe.quotes.update(quote, options,__extra);
};

// /v1/quotes/{quote}/accept - post
exports.acceptQuote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const quote = this.parseRequired(options.quote, 'string', 'stripe.acceptQuote: quote is required.');
  delete options.quote;
  return stripe.quotes.accept(quote, options,__extra);
};

// /v1/quotes/{quote}/cancel - post
exports.cancelQuote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const quote = this.parseRequired(options.quote, 'string', 'stripe.cancelQuote: quote is required.');
  delete options.quote;
  return stripe.quotes.cancel(quote, options,__extra);
};

// /v1/quotes/{quote}/computed_upfront_line_items - get
exports.listQuoteComputedUpfrontLineItems = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const quote = this.parseRequired(options.quote, 'string', 'stripe.listQuoteComputedUpfrontLineItems: quote is required.');
  delete options.quote;
  return stripe.quotes.listComputedUpfrontLineItems(quote, options,__extra);
};

// /v1/quotes/{quote}/finalize - post
exports.finalizeQuote = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const quote = this.parseRequired(options.quote, 'string', 'stripe.finalizeQuote: quote is required.');
  delete options.quote;
  return stripe.quotes.finalizeQuote(quote, options,__extra);
};

// /v1/quotes/{quote}/line_items - get
exports.listQuoteLineItems = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const quote = this.parseRequired(options.quote, 'string', 'stripe.listQuoteLineItems: quote is required.');
  delete options.quote;
  return stripe.quotes.listLineItems(quote, options,__extra);
};

// /v1/quotes/{quote}/pdf - get
exports.retrieveQuotePdf = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const quote = this.parseRequired(options.quote, 'string', 'stripe.retrieveQuotePdf: quote is required.');
  delete options.quote;
  return stripe.quotes.retrievePdf(quote, options,__extra);
};

// /v1/radar/early_fraud_warnings - get
exports.listRadarEarlyFraudWarnings = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.radar.earlyFraudWarnings.list(options,__extra);
};

// /v1/radar/early_fraud_warnings/{early_fraud_warning} - get
exports.retrieveRadarEarlyFraudWarning = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const early_fraud_warning = this.parseRequired(options.early_fraud_warning, 'string', 'stripe.retrieveRadarEarlyFraudWarning: early_fraud_warning is required.');
  delete options.early_fraud_warning;
  return stripe.radar.earlyFraudWarnings.retrieve(early_fraud_warning, options,__extra);
};

// /v1/radar/value_list_items - get
exports.listRadarValueListItems = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const value_list = this.parseRequired(options.value_list, 'string', 'stripe.listRadarValueListItems: value_list is required.');
  return stripe.radar.valueListItems.list(options,__extra);
};

// /v1/radar/value_list_items - post
exports.createRadarValueListItem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.radar.valueListItems.create(options,__extra);
};

// /v1/radar/value_list_items/{item} - delete
exports.deleteRadarValueListItem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const item = this.parseRequired(options.item, 'string', 'stripe.deleteRadarValueListItem: item is required.');
  delete options.item;
  return stripe.radar.valueListItems.del(item, options,__extra);
};

// /v1/radar/value_list_items/{item} - get
exports.retrieveRadarValueListItem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const item = this.parseRequired(options.item, 'string', 'stripe.retrieveRadarValueListItem: item is required.');
  delete options.item;
  return stripe.radar.valueListItems.retrieve(item, options,__extra);
};

// /v1/radar/value_lists - get
exports.listRadarValueLists = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.radar.valueLists.list(options,__extra);
};

// /v1/radar/value_lists - post
exports.createRadarValueList = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.radar.valueLists.create(options,__extra);
};

// /v1/radar/value_lists/{value_list} - delete
exports.deleteRadarValueList = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const value_list = this.parseRequired(options.value_list, 'string', 'stripe.deleteRadarValueList: value_list is required.');
  delete options.value_list;
  return stripe.radar.valueLists.del(value_list, options,__extra);
};

// /v1/radar/value_lists/{value_list} - get
exports.retrieveRadarValueList = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const value_list = this.parseRequired(options.value_list, 'string', 'stripe.retrieveRadarValueList: value_list is required.');
  delete options.value_list;
  return stripe.radar.valueLists.retrieve(value_list, options,__extra);
};

// /v1/radar/value_lists/{value_list} - post
exports.updateRadarValueList = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const value_list = this.parseRequired(options.value_list, 'string', 'stripe.updateRadarValueList: value_list is required.');
  delete options.value_list;
  return stripe.radar.valueLists.update(value_list, options,__extra);
};

// /v1/recipients - get
exports.listRecipients = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.recipients.list(options,__extra);
};

// /v1/recipients - post
exports.createRecipient = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.recipients.create(options,__extra);
};

// /v1/recipients/{id} - delete
exports.deleteRecipient = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.deleteRecipient: id is required.');
  delete options.id;
  return stripe.recipients.del(id, options,__extra);
};

// /v1/recipients/{id} - get
exports.retrieveRecipient = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveRecipient: id is required.');
  delete options.id;
  return stripe.recipients.retrieve(id, options,__extra);
};

// /v1/recipients/{id} - post
exports.updateRecipient = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.updateRecipient: id is required.');
  delete options.id;
  return stripe.recipients.update(id, options,__extra);
};

// /v1/refunds - get
exports.listRefunds = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.refunds.list(options,__extra);
};

// /v1/refunds - post
exports.createRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.refunds.create(options,__extra);
};

// /v1/refunds/{refund} - get
exports.retrieveRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const refund = this.parseRequired(options.refund, 'string', 'stripe.retrieveRefund: refund is required.');
  delete options.refund;
  return stripe.refunds.retrieve(refund, options,__extra);
};

// /v1/refunds/{refund} - post
exports.updateRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const refund = this.parseRequired(options.refund, 'string', 'stripe.updateRefund: refund is required.');
  delete options.refund;
  return stripe.refunds.update(refund, options,__extra);
};

// /v1/refunds/{refund}/cancel - post
exports.cancelRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const refund = this.parseRequired(options.refund, 'string', 'stripe.cancelRefund: refund is required.');
  delete options.refund;
  return stripe.refunds.cancel(refund, options,__extra);
};

// /v1/reporting/report_runs - get
exports.listReportingReportRuns = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.reporting.reportRuns.list(options,__extra);
};

// /v1/reporting/report_runs - post
exports.createReportingReportRun = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.reporting.reportRuns.create(options,__extra);
};

// /v1/reporting/report_runs/{report_run} - get
exports.retrieveReportingReportRun = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const report_run = this.parseRequired(options.report_run, 'string', 'stripe.retrieveReportingReportRun: report_run is required.');
  delete options.report_run;
  return stripe.reporting.reportRuns.retrieve(report_run, options,__extra);
};

// /v1/reporting/report_types - get
exports.listReportingReportTypes = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.reporting.reportTypes.list(options,__extra);
};

// /v1/reporting/report_types/{report_type} - get
exports.retrieveReportingReportType = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const report_type = this.parseRequired(options.report_type, 'string', 'stripe.retrieveReportingReportType: report_type is required.');
  delete options.report_type;
  return stripe.reporting.reportTypes.retrieve(report_type, options,__extra);
};

// /v1/reviews - get
exports.listReviews = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.reviews.list(options,__extra);
};

// /v1/reviews/{review} - get
exports.retrieveReview = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const review = this.parseRequired(options.review, 'string', 'stripe.retrieveReview: review is required.');
  delete options.review;
  return stripe.reviews.retrieve(review, options,__extra);
};

// /v1/reviews/{review}/approve - post
exports.approveReview = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const review = this.parseRequired(options.review, 'string', 'stripe.approveReview: review is required.');
  delete options.review;
  return stripe.reviews.approve(review, options,__extra);
};

// /v1/setup_attempts - get
exports.listSetupAttempts = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const setup_intent = this.parseRequired(options.setup_intent, 'string', 'stripe.listSetupAttempts: setup_intent is required.');
  return stripe.setupAttempts.list(options,__extra);
};

// /v1/setup_intents - get
exports.listSetupIntents = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.setupIntents.list(options,__extra);
};

// /v1/setup_intents - post
exports.createSetupIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.setupIntents.create(options,__extra);
};

// /v1/setup_intents/{intent} - get
exports.retrieveSetupIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.retrieveSetupIntent: intent is required.');
  delete options.intent;
  return stripe.setupIntents.retrieve(intent, options,__extra);
};

// /v1/setup_intents/{intent} - post
exports.updateSetupIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.updateSetupIntent: intent is required.');
  delete options.intent;
  return stripe.setupIntents.update(intent, options,__extra);
};

// /v1/setup_intents/{intent}/cancel - post
exports.cancelSetupIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.cancelSetupIntent: intent is required.');
  delete options.intent;
  return stripe.setupIntents.cancel(intent, options,__extra);
};

// /v1/setup_intents/{intent}/confirm - post
exports.confirmSetupIntent = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.confirmSetupIntent: intent is required.');
  delete options.intent;
  return stripe.setupIntents.confirm(intent, options,__extra);
};

// /v1/setup_intents/{intent}/verify_microdeposits - post
exports.createSetupIntentVerifyMicrodeposit = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const intent = this.parseRequired(options.intent, 'string', 'stripe.createSetupIntentVerifyMicrodeposit: intent is required.');
  delete options.intent;
  return stripe.setupIntents.createVerifyMicrodeposit(intent, options,__extra);
};

// /v1/shipping_rates - get
exports.listShippingRates = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.shippingRates.list(options,__extra);
};

// /v1/shipping_rates - post
exports.createShippingRate = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.shippingRates.create(options,__extra);
};

// /v1/shipping_rates/{shipping_rate_token} - get
exports.retrieveShippingRate = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const shipping_rate_token = this.parseRequired(options.shipping_rate_token, 'string', 'stripe.retrieveShippingRate: shipping_rate_token is required.');
  delete options.shipping_rate_token;
  return stripe.shippingRates.retrieve(shipping_rate_token, options,__extra);
};

// /v1/shipping_rates/{shipping_rate_token} - post
exports.updateShippingRate = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const shipping_rate_token = this.parseRequired(options.shipping_rate_token, 'string', 'stripe.updateShippingRate: shipping_rate_token is required.');
  delete options.shipping_rate_token;
  return stripe.shippingRates.update(shipping_rate_token, options,__extra);
};

// /v1/sigma/scheduled_query_runs - get
exports.listSigmaScheduledQueryRuns = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.sigma.scheduledQueryRuns.list(options,__extra);
};

// /v1/sigma/scheduled_query_runs/{scheduled_query_run} - get
exports.retrieveSigmaScheduledQueryRun = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const scheduled_query_run = this.parseRequired(options.scheduled_query_run, 'string', 'stripe.retrieveSigmaScheduledQueryRun: scheduled_query_run is required.');
  delete options.scheduled_query_run;
  return stripe.sigma.scheduledQueryRuns.retrieve(scheduled_query_run, options,__extra);
};

// /v1/skus - get
exports.listSkus = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.skus.list(options,__extra);
};

// /v1/skus - post
exports.createSku = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.skus.create(options,__extra);
};

// /v1/skus/{id} - delete
exports.deleteSku = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.deleteSku: id is required.');
  delete options.id;
  return stripe.skus.del(id, options,__extra);
};

// /v1/skus/{id} - get
exports.retrieveSku = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveSku: id is required.');
  delete options.id;
  return stripe.skus.retrieve(id, options,__extra);
};

// /v1/skus/{id} - post
exports.updateSku = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.updateSku: id is required.');
  delete options.id;
  return stripe.skus.update(id, options,__extra);
};

// /v1/sources - post
exports.createSource = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.sources.create(options,__extra);
};

// /v1/sources/{source} - get
exports.retrieveSource = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const source = this.parseRequired(options.source, 'string', 'stripe.retrieveSource: source is required.');
  delete options.source;
  return stripe.sources.retrieve(source, options,__extra);
};

// /v1/sources/{source} - post
exports.updateSource = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const source = this.parseRequired(options.source, 'string', 'stripe.updateSource: source is required.');
  delete options.source;
  return stripe.sources.update(source, options,__extra);
};

// /v1/sources/{source}/source_transactions - get
exports.listSourceSourceTransactions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const source = this.parseRequired(options.source, 'string', 'stripe.listSourceSourceTransactions: source is required.');
  delete options.source;
  return stripe.sources.listSourceTransactions(source, options,__extra);
};

// /v1/sources/{source}/verify - post
exports.verifySource = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const source = this.parseRequired(options.source, 'string', 'stripe.verifySource: source is required.');
  delete options.source;
  return stripe.sources.verify(source, options,__extra);
};

// /v1/subscription_items - get
exports.listSubscriptionItems = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const subscription = this.parseRequired(options.subscription, 'string', 'stripe.listSubscriptionItems: subscription is required.');
  return stripe.subscriptionItems.list(options,__extra);
};

// /v1/subscription_items - post
exports.createSubscriptionItem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.subscriptionItems.create(options,__extra);
};

// /v1/subscription_items/{item} - delete
exports.deleteSubscriptionItem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const item = this.parseRequired(options.item, 'string', 'stripe.deleteSubscriptionItem: item is required.');
  delete options.item;
  return stripe.subscriptionItems.del(item, options,__extra);
};

// /v1/subscription_items/{item} - get
exports.retrieveSubscriptionItem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const item = this.parseRequired(options.item, 'string', 'stripe.retrieveSubscriptionItem: item is required.');
  delete options.item;
  return stripe.subscriptionItems.retrieve(item, options,__extra);
};

// /v1/subscription_items/{item} - post
exports.updateSubscriptionItem = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const item = this.parseRequired(options.item, 'string', 'stripe.updateSubscriptionItem: item is required.');
  delete options.item;
  return stripe.subscriptionItems.update(item, options,__extra);
};

// /v1/subscription_items/{subscription_item}/usage_record_summaries - get
exports.listSubscriptionItemUsageRecordSummaries = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const subscription_item = this.parseRequired(options.subscription_item, 'string', 'stripe.listSubscriptionItemUsageRecordSummaries: subscription_item is required.');
  delete options.subscription_item;
  return stripe.subscriptionItems.listUsageRecordSummaries(subscription_item, options,__extra);
};

// /v1/subscription_items/{subscription_item}/usage_records - post
exports.createSubscriptionItemUsageRecord = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const subscription_item = this.parseRequired(options.subscription_item, 'string', 'stripe.createSubscriptionItemUsageRecord: subscription_item is required.');
  delete options.subscription_item;
  return stripe.subscriptionItems.createUsageRecord(subscription_item, options,__extra);
};

// /v1/subscription_schedules - get
exports.listSubscriptionSchedules = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.subscriptionSchedules.list(options,__extra);
};

// /v1/subscription_schedules - post
exports.createSubscriptionSchedule = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.subscriptionSchedules.create(options,__extra);
};

// /v1/subscription_schedules/{schedule} - get
exports.retrieveSubscriptionSchedule = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const schedule = this.parseRequired(options.schedule, 'string', 'stripe.retrieveSubscriptionSchedule: schedule is required.');
  delete options.schedule;
  return stripe.subscriptionSchedules.retrieve(schedule, options,__extra);
};

// /v1/subscription_schedules/{schedule} - post
exports.updateSubscriptionSchedule = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const schedule = this.parseRequired(options.schedule, 'string', 'stripe.updateSubscriptionSchedule: schedule is required.');
  delete options.schedule;
  return stripe.subscriptionSchedules.update(schedule, options,__extra);
};

// /v1/subscription_schedules/{schedule}/cancel - post
exports.cancelSubscriptionSchedule = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const schedule = this.parseRequired(options.schedule, 'string', 'stripe.cancelSubscriptionSchedule: schedule is required.');
  delete options.schedule;
  return stripe.subscriptionSchedules.cancel(schedule, options,__extra);
};

// /v1/subscription_schedules/{schedule}/release - post
exports.releaseSubscriptionSchedule = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const schedule = this.parseRequired(options.schedule, 'string', 'stripe.releaseSubscriptionSchedule: schedule is required.');
  delete options.schedule;
  return stripe.subscriptionSchedules.release(schedule, options,__extra);
};

// /v1/subscriptions - get
exports.listSubscriptions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.subscriptions.list(options,__extra);
};

// /v1/subscriptions - post
exports.createSubscription = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.subscriptions.create(options,__extra);
};

// /v1/subscriptions/search - get
exports.searchSubscriptions = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const query = this.parseRequired(options.query, 'string', 'stripe.searchSubscriptions: query is required.');
  return stripe.subscriptions.search(options,__extra);
};

// /v1/subscriptions/{subscription_exposed_id} - delete
exports.deleteSubscription = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const subscription_exposed_id = this.parseRequired(options.subscription_exposed_id, 'string', 'stripe.deleteSubscription: subscription_exposed_id is required.');
  delete options.subscription_exposed_id;
  return stripe.subscriptions.del(subscription_exposed_id, options,__extra);
};

// /v1/subscriptions/{subscription_exposed_id} - get
exports.retrieveSubscription = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const subscription_exposed_id = this.parseRequired(options.subscription_exposed_id, 'string', 'stripe.retrieveSubscription: subscription_exposed_id is required.');
  delete options.subscription_exposed_id;
  return stripe.subscriptions.retrieve(subscription_exposed_id, options,__extra);
};

// /v1/subscriptions/{subscription_exposed_id} - post
exports.updateSubscription = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const subscription_exposed_id = this.parseRequired(options.subscription_exposed_id, 'string', 'stripe.updateSubscription: subscription_exposed_id is required.');
  delete options.subscription_exposed_id;
  return stripe.subscriptions.update(subscription_exposed_id, options,__extra);
};

// /v1/subscriptions/{subscription_exposed_id}/discount - delete
exports.deleteSubscriptionDiscount = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const subscription_exposed_id = this.parseRequired(options.subscription_exposed_id, 'string', 'stripe.deleteSubscriptionDiscount: subscription_exposed_id is required.');
  delete options.subscription_exposed_id;
  return stripe.subscriptions.deleteDiscount(subscription_exposed_id, options,__extra);
};

// /v1/tax_codes - get
exports.listTaxCodes = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.taxCodes.list(options,__extra);
};

// /v1/tax_codes/{id} - get
exports.retrieveTaxCode = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveTaxCode: id is required.');
  delete options.id;
  return stripe.taxCodes.retrieve(id, options,__extra);
};

// /v1/tax_rates - get
exports.listTaxRates = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.taxRates.list(options,__extra);
};

// /v1/tax_rates - post
exports.createTaxRate = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.taxRates.create(options,__extra);
};

// /v1/tax_rates/{tax_rate} - get
exports.retrieveTaxRate = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const tax_rate = this.parseRequired(options.tax_rate, 'string', 'stripe.retrieveTaxRate: tax_rate is required.');
  delete options.tax_rate;
  return stripe.taxRates.retrieve(tax_rate, options,__extra);
};

// /v1/tax_rates/{tax_rate} - post
exports.updateTaxRate = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const tax_rate = this.parseRequired(options.tax_rate, 'string', 'stripe.updateTaxRate: tax_rate is required.');
  delete options.tax_rate;
  return stripe.taxRates.update(tax_rate, options,__extra);
};

// /v1/terminal/configurations - get
exports.listTerminalConfigurations = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.terminal.configurations.list(options,__extra);
};

// /v1/terminal/configurations - post
exports.createTerminalConfiguration = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.terminal.configurations.create(options,__extra);
};

// /v1/terminal/configurations/{configuration} - delete
exports.deleteTerminalConfiguration = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const configuration = this.parseRequired(options.configuration, 'string', 'stripe.deleteTerminalConfiguration: configuration is required.');
  delete options.configuration;
  return stripe.terminal.configurations.del(configuration, options,__extra);
};

// /v1/terminal/configurations/{configuration} - get
exports.retrieveTerminalConfiguration = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const configuration = this.parseRequired(options.configuration, 'string', 'stripe.retrieveTerminalConfiguration: configuration is required.');
  delete options.configuration;
  return stripe.terminal.configurations.retrieve(configuration, options,__extra);
};

// /v1/terminal/configurations/{configuration} - post
exports.updateTerminalConfiguration = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const configuration = this.parseRequired(options.configuration, 'string', 'stripe.updateTerminalConfiguration: configuration is required.');
  delete options.configuration;
  return stripe.terminal.configurations.update(configuration, options,__extra);
};

// /v1/terminal/connection_tokens - post
exports.createTerminalConnectionToken = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.terminal.connectionTokens.create(options,__extra);
};

// /v1/terminal/locations - get
exports.listTerminalLocations = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.terminal.locations.list(options,__extra);
};

// /v1/terminal/locations - post
exports.createTerminalLocation = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.terminal.locations.create(options,__extra);
};

// /v1/terminal/locations/{location} - delete
exports.deleteTerminalLocation = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const location = this.parseRequired(options.location, 'string', 'stripe.deleteTerminalLocation: location is required.');
  delete options.location;
  return stripe.terminal.locations.del(location, options,__extra);
};

// /v1/terminal/locations/{location} - get
exports.retrieveTerminalLocation = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const location = this.parseRequired(options.location, 'string', 'stripe.retrieveTerminalLocation: location is required.');
  delete options.location;
  return stripe.terminal.locations.retrieve(location, options,__extra);
};

// /v1/terminal/locations/{location} - post
exports.updateTerminalLocation = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const location = this.parseRequired(options.location, 'string', 'stripe.updateTerminalLocation: location is required.');
  delete options.location;
  return stripe.terminal.locations.update(location, options,__extra);
};

// /v1/terminal/readers - get
exports.listTerminalReaders = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.terminal.readers.list(options,__extra);
};

// /v1/terminal/readers - post
exports.createTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.terminal.readers.create(options,__extra);
};

// /v1/terminal/readers/{reader} - delete
exports.deleteTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const reader = this.parseRequired(options.reader, 'string', 'stripe.deleteTerminalReader: reader is required.');
  delete options.reader;
  return stripe.terminal.readers.del(reader, options,__extra);
};

// /v1/terminal/readers/{reader} - get
exports.retrieveTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const reader = this.parseRequired(options.reader, 'string', 'stripe.retrieveTerminalReader: reader is required.');
  delete options.reader;
  return stripe.terminal.readers.retrieve(reader, options,__extra);
};

// /v1/terminal/readers/{reader} - post
exports.updateTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const reader = this.parseRequired(options.reader, 'string', 'stripe.updateTerminalReader: reader is required.');
  delete options.reader;
  return stripe.terminal.readers.update(reader, options,__extra);
};

// /v1/terminal/readers/{reader}/cancel_action - post
exports.cancelActionTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const reader = this.parseRequired(options.reader, 'string', 'stripe.cancelActionTerminalReader: reader is required.');
  delete options.reader;
  return stripe.terminal.readers.cancelAction(reader, options,__extra);
};

// /v1/terminal/readers/{reader}/process_payment_intent - post
exports.processPaymentIntentTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const reader = this.parseRequired(options.reader, 'string', 'stripe.processPaymentIntentTerminalReader: reader is required.');
  delete options.reader;
  return stripe.terminal.readers.processPaymentIntent(reader, options,__extra);
};

// /v1/terminal/readers/{reader}/process_setup_intent - post
exports.processSetupIntentTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const reader = this.parseRequired(options.reader, 'string', 'stripe.processSetupIntentTerminalReader: reader is required.');
  delete options.reader;
  return stripe.terminal.readers.processSetupIntent(reader, options,__extra);
};

// /v1/terminal/readers/{reader}/set_reader_display - post
exports.setReaderDisplayTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const reader = this.parseRequired(options.reader, 'string', 'stripe.setReaderDisplayTerminalReader: reader is required.');
  delete options.reader;
  return stripe.terminal.readers.setReaderDisplay(reader, options,__extra);
};

// /v1/test_helpers/refunds/{refund}/expire - post
exports.expireTestHelpersRefund = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const refund = this.parseRequired(options.refund, 'string', 'stripe.expireTestHelpersRefund: refund is required.');
  delete options.refund;
  return stripe.testHelpers.refunds.expire(refund, options,__extra);
};

// /v1/test_helpers/terminal/readers/{reader}/present_payment_method - post
exports.presentPaymentMethodTestHelpersTerminalReader = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const reader = this.parseRequired(options.reader, 'string', 'stripe.presentPaymentMethodTestHelpersTerminalReader: reader is required.');
  delete options.reader;
  return stripe.testHelpers.terminal.readers.presentPaymentMethod(reader, options,__extra);
};

// /v1/test_helpers/test_clocks - get
exports.listTestHelpersTestClocks = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.testHelpers.testClocks.list(options,__extra);
};

// /v1/test_helpers/test_clocks - post
exports.createTestHelpersTestClock = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.testHelpers.testClocks.create(options,__extra);
};

// /v1/test_helpers/test_clocks/{test_clock} - delete
exports.deleteTestHelpersTestClock = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const test_clock = this.parseRequired(options.test_clock, 'string', 'stripe.deleteTestHelpersTestClock: test_clock is required.');
  delete options.test_clock;
  return stripe.testHelpers.testClocks.del(test_clock, options,__extra);
};

// /v1/test_helpers/test_clocks/{test_clock} - get
exports.retrieveTestHelpersTestClock = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const test_clock = this.parseRequired(options.test_clock, 'string', 'stripe.retrieveTestHelpersTestClock: test_clock is required.');
  delete options.test_clock;
  return stripe.testHelpers.testClocks.retrieve(test_clock, options,__extra);
};

// /v1/test_helpers/test_clocks/{test_clock}/advance - post
exports.advanceTestHelpersTestClock = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const test_clock = this.parseRequired(options.test_clock, 'string', 'stripe.advanceTestHelpersTestClock: test_clock is required.');
  delete options.test_clock;
  return stripe.testHelpers.testClocks.advance(test_clock, options,__extra);
};

// /v1/tokens - post
exports.createToken = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.tokens.create(options,__extra);
};

// /v1/tokens/{token} - get
exports.retrieveToken = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const token = this.parseRequired(options.token, 'string', 'stripe.retrieveToken: token is required.');
  delete options.token;
  return stripe.tokens.retrieve(token, options,__extra);
};

// /v1/topups - get
exports.listTopups = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.topups.list(options,__extra);
};

// /v1/topups - post
exports.createTopup = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.topups.create(options,__extra);
};

// /v1/topups/{topup} - get
exports.retrieveTopup = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const topup = this.parseRequired(options.topup, 'string', 'stripe.retrieveTopup: topup is required.');
  delete options.topup;
  return stripe.topups.retrieve(topup, options,__extra);
};

// /v1/topups/{topup} - post
exports.updateTopup = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const topup = this.parseRequired(options.topup, 'string', 'stripe.updateTopup: topup is required.');
  delete options.topup;
  return stripe.topups.update(topup, options,__extra);
};

// /v1/topups/{topup}/cancel - post
exports.cancelTopup = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const topup = this.parseRequired(options.topup, 'string', 'stripe.cancelTopup: topup is required.');
  delete options.topup;
  return stripe.topups.cancel(topup, options,__extra);
};

// /v1/transfers - get
exports.listTransfers = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.transfers.list(options,__extra);
};

// /v1/transfers - post
exports.createTransfer = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.transfers.create(options,__extra);
};

// /v1/transfers/{id}/reversals - get
exports.listTransferReversals = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.listTransferReversals: id is required.');
  delete options.id;
  return stripe.transfers.listReversals(id, options,__extra);
};

// /v1/transfers/{id}/reversals - post
exports.createTransferReversal = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.createTransferReversal: id is required.');
  delete options.id;
  return stripe.transfers.createReversal(id, options,__extra);
};

// /v1/transfers/{transfer} - get
exports.retrieveTransfer = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const transfer = this.parseRequired(options.transfer, 'string', 'stripe.retrieveTransfer: transfer is required.');
  delete options.transfer;
  return stripe.transfers.retrieve(transfer, options,__extra);
};

// /v1/transfers/{transfer} - post
exports.updateTransfer = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const transfer = this.parseRequired(options.transfer, 'string', 'stripe.updateTransfer: transfer is required.');
  delete options.transfer;
  return stripe.transfers.update(transfer, options,__extra);
};

// /v1/transfers/{transfer}/reversals/{id} - get
exports.retrieveTransferReversal = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.retrieveTransferReversal: id is required.');
  delete options.id;
  const transfer = this.parseRequired(options.transfer, 'string', 'stripe.retrieveTransferReversal: transfer is required.');
  delete options.transfer;
  return stripe.transfers.retrieveReversal(id, transfer, options,__extra);
};

// /v1/transfers/{transfer}/reversals/{id} - post
exports.updateTransferReversal = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const id = this.parseRequired(options.id, 'string', 'stripe.updateTransferReversal: id is required.');
  delete options.id;
  const transfer = this.parseRequired(options.transfer, 'string', 'stripe.updateTransferReversal: transfer is required.');
  delete options.transfer;
  return stripe.transfers.updateReversal(id, transfer, options,__extra);
};

// /v1/webhook_endpoints - get
exports.listWebhookEndpoints = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.webhookEndpoints.list(options,__extra);
};

// /v1/webhook_endpoints - post
exports.createWebhookEndpoint = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  return stripe.webhookEndpoints.create(options,__extra);
};

// /v1/webhook_endpoints/{webhook_endpoint} - delete
exports.deleteWebhookEndpoint = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const webhook_endpoint = this.parseRequired(options.webhook_endpoint, 'string', 'stripe.deleteWebhookEndpoint: webhook_endpoint is required.');
  delete options.webhook_endpoint;
  return stripe.webhookEndpoints.del(webhook_endpoint, options,__extra);
};

// /v1/webhook_endpoints/{webhook_endpoint} - get
exports.retrieveWebhookEndpoint = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const webhook_endpoint = this.parseRequired(options.webhook_endpoint, 'string', 'stripe.retrieveWebhookEndpoint: webhook_endpoint is required.');
  delete options.webhook_endpoint;
  return stripe.webhookEndpoints.retrieve(webhook_endpoint, options,__extra);
};

// /v1/webhook_endpoints/{webhook_endpoint} - post
exports.updateWebhookEndpoint = function(options) {
  options = this.parse(options);
  var __extra = options.__extra;
  if (options.__extra) {
    __extra = convertExtraOptions(__extra);
    delete options.__extra;
  }

  const webhook_endpoint = this.parseRequired(options.webhook_endpoint, 'string', 'stripe.updateWebhookEndpoint: webhook_endpoint is required.');
  delete options.webhook_endpoint;
  return stripe.webhookEndpoints.update(webhook_endpoint, options,__extra);
};
